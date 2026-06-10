function report = palette_validator(palette, varargin)
%PALETTE_VALIDATOR  调色板全方位体检.
%
%   报告 = palette_validator(palette)
%   返回 struct，含: dE_normal, dE_proto, dE_deut, dE_trit, gray_dL, ok
%   并打印可读体检报告。
%
%   palette : N×3 RGB 矩阵或 cell array of hex
%
    if iscell(palette)
        rgbs = zeros(numel(palette), 3);
        for i = 1:numel(palette), rgbs(i, :) = color_lab('hex2rgb', palette{i}); end
        palette = rgbs;
    end
    n = size(palette, 1);

    % 两两 CIEDE2000 最小色差
    function d = min_pair_dE(P)
        d = Inf;
        for i = 1:size(P,1)-1
            for j = i+1:size(P,1)
                lab1 = color_lab('rgb2lab', P(i,:));
                lab2 = color_lab('rgb2lab', P(j,:));
                d = min(d, color_lab('deltaE2000', lab1, lab2));
            end
        end
    end

    report.dE_normal = min_pair_dE(palette);

    % CVD 下
    P_proto = palette; P_deut = palette; P_trit = palette;
    for i = 1:n
        P_proto(i, :) = color_lab('cvd', palette(i, :), 'protanopia');
        P_deut(i, :)  = color_lab('cvd', palette(i, :), 'deuteranopia');
        P_trit(i, :)  = color_lab('cvd', palette(i, :), 'tritanopia');
    end
    report.dE_proto = min_pair_dE(P_proto);
    report.dE_deut  = min_pair_dE(P_deut);
    report.dE_trit  = min_pair_dE(P_trit);

    [report.ok_gray, report.gray_dL] = color_lab('grayscale_safe', palette);

    report.ok = report.dE_normal > 15 && ...
                report.dE_proto > 9 && report.dE_deut > 9 && ...
                report.gray_dL > 15;

    % 打印
    fprintf('调色板（%d 色）体检报告\n', n);
    fprintf('— CIEDE2000 两两最小色差（>15 为良好）\n');
    fprintf('  正常视觉      : %5.1f  %s\n', report.dE_normal, grade_(report.dE_normal));
    fprintf('  红色盲(proto.): %5.1f  %s\n', report.dE_proto,  grade_(report.dE_proto));
    fprintf('  绿色盲(deut.) : %5.1f  %s\n', report.dE_deut,   grade_(report.dE_deut));
    fprintf('  蓝色盲(trit.) : %5.1f  %s\n', report.dE_trit,   grade_(report.dE_trit));
    fprintf('— 灰度安全 ΔL = %5.1f  %s\n', report.gray_dL, ...
            ternary_(report.ok_gray, '✓', '✗'));
    fprintf('总评 : %s\n', ternary_(report.ok, '✓ 通过', '✗ 未通过'));
end

function s = grade_(d)
    if d > 30, s = '优秀';
    elseif d > 15, s = '良好';
    elseif d > 5, s = '勉强';
    else, s = '不行'; end
end

function s = ternary_(cond, a, b)
    if cond, s = a; else, s = b; end
end
