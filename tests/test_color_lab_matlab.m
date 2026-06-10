function test_color_lab_matlab()
%TEST_COLOR_LAB_MATLAB  跨语言一致性测试.
%   读取 Python 端生成的 golden 值，逐项断言 MATLAB color_lab 实现一致。
%
%   用法（命令行）:
%     cd 科研绘图_函数库
%     matlab -batch "addpath('palettes/matlab'); test_color_lab_matlab"
%
%   也可在 MATLAB 里直接 run('tests/test_color_lab_matlab.m')。
    here = fileparts(mfilename('fullpath'));
    root = fullfile(here, '..');
    addpath(fullfile(root, 'palettes', 'matlab'));

    golden_file = fullfile(here, 'golden_color_math.json');
    if ~exist(golden_file, 'file')
        error(['未找到 ' golden_file '\n请先在 Python 端运行:\n' ...
               '    python tests/generate_golden.py']);
    end

    txt = fileread(golden_file);
    G = jsondecode(txt);

    tol = G.meta.tolerance_recommended;
    n_pass = 0; n_fail = 0;
    fails = {};

    function check(label, actual, expected, t)
        if nargin < 4, t = tol; end
        actual = double(actual(:).');
        expected = double(expected(:).');
        if numel(actual) ~= numel(expected)
            err = inf;
        else
            err = max(abs(actual - expected));
        end
        if err <= t
            n_pass = n_pass + 1;
        else
            n_fail = n_fail + 1;
            fails{end+1} = sprintf('%s: err=%.2e (tol=%.2e)', label, err, t);
        end
    end

    fprintf('=== Python ↔ MATLAB color math 一致性测试 ===\n');
    fprintf('Loaded %d cases + %d pairs (tol=%.0e)\n\n', ...
            numel(G.cases), numel(G.pairs), tol);

    for k = 1:numel(G.cases)
        c = G.cases(k);
        rgb = color_lab('hex2rgb', char(c.hex));
        check(sprintf('%s hex2rgb', c.hex), rgb, c.rgb);

        lab = color_lab('rgb2lab', rgb);
        check(sprintf('%s rgb2lab', c.hex), lab, c.lab, 1e-3);

        lch = color_lab('lab2lch', lab);
        check(sprintf('%s lab2lch', c.hex), lch, c.lch, 1e-2);

        Y = color_lab('luminance', rgb);
        check(sprintf('%s luminance', c.hex), Y, c.luminance);

        rgb_back = color_lab('lab2rgb', lab);
        check(sprintf('%s lab2rgb', c.hex), rgb_back, c.lab_to_srgb, 1e-3);

        cvd_d = color_lab('cvd', rgb, 'deuteranopia');
        check(sprintf('%s cvd deut', c.hex), cvd_d, c.cvd_deut, 1e-3);

        cvd_p = color_lab('cvd', rgb, 'protanopia');
        check(sprintf('%s cvd proto', c.hex), cvd_p, c.cvd_proto, 1e-3);
    end

    for k = 1:numel(G.pairs)
        p = G.pairs(k);
        rgb1 = color_lab('hex2rgb', char(p.hex1));
        rgb2 = color_lab('hex2rgb', char(p.hex2));
        lab1 = color_lab('rgb2lab', rgb1);
        lab2 = color_lab('rgb2lab', rgb2);

        dE = color_lab('deltaE2000', lab1, lab2);
        check(sprintf('%s↔%s ΔE2000', p.hex1, p.hex2), dE, p.delta_e_2000, 1e-2);

        cr = color_lab('contrast', rgb1, rgb2);
        check(sprintf('%s↔%s contrast', p.hex1, p.hex2), cr, p.contrast_ratio, 1e-3);
    end

    fprintf('PASS: %d\nFAIL: %d\n', n_pass, n_fail);
    if n_fail > 0
        fprintf('\nFailures:\n');
        for i = 1:numel(fails), fprintf('  %s\n', fails{i}); end
        error('MATLAB 实现与 Python 不一致');
    else
        fprintf('\n✓ MATLAB color_lab 与 Python 一致\n');
    end
end
