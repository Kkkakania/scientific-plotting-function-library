function out = color_lab(op, varargin)
%COLOR_LAB  色彩科学工具（MATLAB 镜像）.
%   实现 sRGB ↔ XYZ ↔ Lab ↔ LCh 的 CIE 标准转换、CIEDE2000 色差、
%   WCAG 对比度、Brettel/Viénot/Mollon 色觉缺陷模拟、灰度安全检查。
%
%   用法:
%     rgb = color_lab('hex2rgb', '#0072B2')         % → [0.0 0.447 0.698]
%     hex = color_lab('rgb2hex', [0 0.4 0.7])       % → '#0066B3'
%     lab = color_lab('rgb2lab', rgb)
%     rgb = color_lab('lab2rgb', lab)
%     lch = color_lab('lab2lch', lab)
%     lab = color_lab('lch2lab', lch)
%     dE  = color_lab('deltaE2000', lab1, lab2)
%     cr  = color_lab('contrast', rgb1, rgb2)       % WCAG
%     sim = color_lab('cvd', rgb, 'deuteranopia')   % 色觉缺陷模拟
%     L   = color_lab('luminance', rgb)             % Rec. 709 亮度
%
    switch lower(op)
        case 'hex2rgb',    out = hex2rgb_(varargin{1});
        case 'rgb2hex',    out = rgb2hex_(varargin{1});
        case 'rgb2lab',    out = rgb2lab_(varargin{1});
        case 'lab2rgb',    out = lab2rgb_(varargin{1});
        case 'lab2lch',    out = lab2lch_(varargin{1});
        case 'lch2lab',    out = lch2lab_(varargin{1});
        case 'deltae76',   out = deltaE76_(varargin{1}, varargin{2});
        case 'deltae2000', out = deltaE2000_(varargin{1}, varargin{2});
        case 'contrast',   out = contrast_(varargin{1}, varargin{2});
        case 'wcag',       out = wcag_(varargin{1}, varargin{2});
        case 'luminance',  out = luminance_(varargin{1});
        case 'cvd',        out = cvd_(varargin{1}, varargin{2});
        case 'grayscale_safe', out = gray_safe_(varargin{1});
        otherwise, error('unknown op: %s', op);
    end
end

% ============== HEX ↔ RGB ==============
function rgb = hex2rgb_(h)
    if h(1) == '#', h = h(2:end); end
    rgb = [hex2dec(h(1:2)) hex2dec(h(3:4)) hex2dec(h(5:6))] / 255;
end
function h = rgb2hex_(rgb)
    rgb = max(0, min(1, rgb));
    h = sprintf('#%02X%02X%02X', round(rgb(1)*255), round(rgb(2)*255), round(rgb(3)*255));
end

% ============== sRGB ↔ Lab ==============
function lin = gamma_inv_(c)
    lin = zeros(size(c));
    mask = c <= 0.04045;
    lin(mask)  = c(mask) / 12.92;
    lin(~mask) = ((c(~mask) + 0.055) / 1.055) .^ 2.4;
end
function c = gamma_(lin)
    lin = max(0, lin);
    c = zeros(size(lin));
    mask = lin <= 0.0031308;
    c(mask)  = lin(mask) * 12.92;
    c(~mask) = 1.055 * lin(~mask).^(1/2.4) - 0.055;
end

function lab = rgb2lab_(rgb)
    M = [0.4124564 0.3575761 0.1804375;
         0.2126729 0.7151522 0.0721750;
         0.0193339 0.1191920 0.9503041];
    lin = gamma_inv_(rgb(:).');
    xyz = lin * M.';
    Xn = 0.95047; Yn = 1.0; Zn = 1.08883;
    fx = f_(xyz(1)/Xn); fy = f_(xyz(2)/Yn); fz = f_(xyz(3)/Zn);
    lab = [116*fy - 16, 500*(fx - fy), 200*(fy - fz)];
end
function rgb = lab2rgb_(lab)
    M = [0.4124564 0.3575761 0.1804375;
         0.2126729 0.7151522 0.0721750;
         0.0193339 0.1191920 0.9503041];
    Minv = inv(M);
    Xn = 0.95047; Yn = 1.0; Zn = 1.08883;
    fy = (lab(1) + 16) / 116;
    fx = fy + lab(2)/500;
    fz = fy - lab(3)/200;
    xyz = [Xn*finv_(fx) Yn*finv_(fy) Zn*finv_(fz)];
    lin = xyz * Minv.';
    rgb = max(0, min(1, gamma_(lin)));
end
function v = f_(t)
    d = 6/29;
    if t > d^3, v = t^(1/3); else, v = t/(3*d^2) + 4/29; end
end
function t = finv_(v)
    d = 6/29;
    if v > d, t = v^3; else, t = 3*d^2*(v - 4/29); end
end

% ============== Lab ↔ LCh ==============
function lch = lab2lch_(lab)
    C = hypot(lab(2), lab(3));
    h = mod(atan2d(lab(3), lab(2)), 360);
    lch = [lab(1) C h];
end
function lab = lch2lab_(lch)
    a = lch(2) * cosd(lch(3));
    b = lch(2) * sind(lch(3));
    lab = [lch(1) a b];
end

% ============== 色差 ==============
function dE = deltaE76_(lab1, lab2)
    dE = norm(lab1 - lab2);
end
function dE = deltaE2000_(lab1, lab2)
    L1 = lab1(1); a1 = lab1(2); b1 = lab1(3);
    L2 = lab2(1); a2 = lab2(2); b2 = lab2(3);
    C1 = hypot(a1, b1); C2 = hypot(a2, b2);
    Cbar = (C1 + C2)/2;
    G = 0.5*(1 - sqrt(Cbar^7 / (Cbar^7 + 25^7)));
    a1p = (1+G)*a1; a2p = (1+G)*a2;
    C1p = hypot(a1p, b1); C2p = hypot(a2p, b2);
    h1p = mod(atan2d(b1, a1p), 360);
    h2p = mod(atan2d(b2, a2p), 360);
    dLp = L2 - L1; dCp = C2p - C1p;
    dhp = h2p - h1p;
    if dhp > 180, dhp = dhp - 360; elseif dhp < -180, dhp = dhp + 360; end
    dHp = 2*sqrt(C1p*C2p)*sind(dhp/2);
    Lbarp = (L1 + L2)/2; Cbarp = (C1p + C2p)/2;
    if abs(h1p - h2p) > 180, hbarp = (h1p + h2p)/2 + 180;
    else, hbarp = (h1p + h2p)/2; end
    T = 1 - 0.17*cosd(hbarp - 30) + 0.24*cosd(2*hbarp) ...
          + 0.32*cosd(3*hbarp + 6) - 0.20*cosd(4*hbarp - 63);
    SL = 1 + (0.015*(Lbarp - 50)^2) / sqrt(20 + (Lbarp - 50)^2);
    SC = 1 + 0.045*Cbarp;
    SH = 1 + 0.015*Cbarp*T;
    dTh = 30*exp(-((hbarp - 275)/25)^2);
    RC = 2*sqrt(Cbarp^7 / (Cbarp^7 + 25^7));
    RT = -RC*sind(2*dTh);
    dE = sqrt((dLp/SL)^2 + (dCp/SC)^2 + (dHp/SH)^2 + RT*(dCp/SC)*(dHp/SH));
end

% ============== WCAG ==============
function L = luminance_(rgb)
    lin = gamma_inv_(rgb);
    L = 0.2126*lin(1) + 0.7152*lin(2) + 0.0722*lin(3);
end
function cr = contrast_(rgb1, rgb2)
    L1 = luminance_(rgb1); L2 = luminance_(rgb2);
    cr = (max(L1, L2) + 0.05) / (min(L1, L2) + 0.05);
end
function lvl = wcag_(rgb1, rgb2)
    cr = contrast_(rgb1, rgb2);
    if cr >= 7, lvl = 'AAA';
    elseif cr >= 4.5, lvl = 'AA';
    else, lvl = 'FAIL'; end
end

% ============== CVD 模拟 ==============
function out = cvd_(rgb, kind)
    mats = struct( ...
        'protanopia',   [ 0.152286  1.052583 -0.204868;
                          0.114503  0.786281  0.099216;
                         -0.003882 -0.048116  1.051998], ...
        'deuteranopia', [ 0.367322  0.860646 -0.227968;
                          0.280085  0.672501  0.047413;
                         -0.011820  0.042940  0.968881], ...
        'tritanopia',   [ 1.255528 -0.076749 -0.178779;
                         -0.078411  0.930809  0.147602;
                          0.004733  0.691367  0.303900]);
    if strcmpi(kind, 'achromatopsia')
        L = luminance_(rgb); out = [L L L]; return;
    end
    M = mats.(lower(kind));
    lin = gamma_inv_(rgb);
    sim_lin = max(0, min(1, lin * M.'));
    out = gamma_(sim_lin);
end

% ============== 灰度安全 ==============
function [ok, min_dL] = gray_safe_(palette)
    n = size(palette, 1);
    Ls = zeros(1, n);
    for i = 1:n, lab = rgb2lab_(palette(i, :)); Ls(i) = lab(1); end
    diffs = abs(Ls.' - Ls);
    diffs(eye(n, 'logical')) = Inf;
    min_dL = min(diffs(:));
    ok = min_dL >= 15;
end
