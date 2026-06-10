function out = palette_generator(kind, varargin)
%PALETTE_GENERATOR  程序化生成感知均匀调色板.
%
%   colors = palette_generator('qualitative', 'n', 8, 'L', 60, 'C', 70)
%   cmap   = palette_generator('sequential',  'n', 256, 'hue', 240)
%   cmap   = palette_generator('diverging',   'n', 256, 'hue_neg', 240, 'hue_pos', 10)
%   hexes  = palette_generator('harmony', 'base', '#0072B2', 'kind', 'triadic')
%
    p = inputParser;
    addParameter(p, 'n', 8);
    addParameter(p, 'L', 60);
    addParameter(p, 'C', 70);
    addParameter(p, 'L_range', [95 25]);
    addParameter(p, 'C_max', 70);
    addParameter(p, 'C_min', 10);
    addParameter(p, 'hue', 240);
    addParameter(p, 'hue_neg', 240);
    addParameter(p, 'hue_pos', 10);
    addParameter(p, 'L_mid', 97);
    addParameter(p, 'L_end', 30);
    addParameter(p, 'h_start', 15);
    addParameter(p, 'h_range', 360);
    addParameter(p, 'base', '#0072B2');
    addParameter(p, 'sub_kind', 'triadic');
    parse(p, varargin{:});
    o = p.Results;

    switch lower(kind)
        case 'qualitative'
            hues = mod(o.h_start + (0:o.n-1) * (o.h_range / o.n), 360);
            out = zeros(o.n, 3);
            for i = 1:o.n
                out(i, :) = color_lab('lab2rgb', color_lab('lch2lab', [o.L o.C hues(i)]));
            end

        case 'sequential'
            t = linspace(0, 1, o.n).';
            L = o.L_range(1) + (o.L_range(2) - o.L_range(1)) * t;
            C = o.C_min + (o.C_max - o.C_min) * (1 - abs(2*t - 1).^1).^0.7;
            h = ones(o.n, 1) * o.hue;
            out = zeros(o.n, 3);
            for i = 1:o.n
                out(i, :) = color_lab('lab2rgb', color_lab('lch2lab', [L(i) C(i) h(i)]));
            end

        case 'diverging'
            t = linspace(-1, 1, o.n).';
            a = abs(t);
            L = o.L_mid - (o.L_mid - o.L_end) * a;
            C = o.C_max * a;
            h = zeros(o.n, 1);
            h(t < 0) = o.hue_neg; h(t >= 0) = o.hue_pos;
            out = zeros(o.n, 3);
            for i = 1:o.n
                out(i, :) = color_lab('lab2rgb', color_lab('lch2lab', [L(i) C(i) h(i)]));
            end

        case 'harmony'
            rgb = color_lab('hex2rgb', o.base);
            lch = color_lab('lab2lch', color_lab('rgb2lab', rgb));
            L = lch(1); C = lch(2); h0 = lch(3);
            switch lower(o.sub_kind)
                case 'complementary',    hues = [h0, mod(h0+180, 360)];
                case 'analogous',        hues = [mod(h0-30, 360), h0, mod(h0+30, 360)];
                case 'triadic',          hues = [h0, mod(h0+120, 360), mod(h0+240, 360)];
                case 'tetradic',         hues = [h0, mod(h0+90, 360), mod(h0+180, 360), mod(h0+270, 360)];
                case 'split_complement', hues = [h0, mod(h0+150, 360), mod(h0+210, 360)];
                otherwise, error('unknown harmony: %s', o.sub_kind);
            end
            hexes = cell(1, numel(hues));
            for i = 1:numel(hues)
                rgb_i = color_lab('lab2rgb', color_lab('lch2lab', [L C hues(i)]));
                hexes{i} = color_lab('rgb2hex', rgb_i);
            end
            out = hexes;

        otherwise
            error('unknown kind: %s', kind);
    end
end
