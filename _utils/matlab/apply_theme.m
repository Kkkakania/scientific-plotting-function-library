function apply_theme(font_size, mode)
%APPLY_THEME  统一论文风格；apply_theme(9, 'dark') 切深色模式
%   深色模式建议配合 sci_palettes 的 dark_bright7 / dark_muted6 /
%   dark_lumen / dark_div 使用。
    if nargin < 1 || isempty(font_size), font_size = 9; end
    if nargin < 2, mode = 'light'; end
    set(groot, 'DefaultFigurePosition',       [100 100 600 400]);
    set(groot, 'DefaultAxesFontName',         'Arial');
    set(groot, 'DefaultAxesFontSize',         font_size);
    set(groot, 'DefaultAxesLineWidth',        0.8);
    set(groot, 'DefaultAxesBox',              'on');
    set(groot, 'DefaultAxesTickDir',          'out');
    set(groot, 'DefaultAxesGridLineStyle',    ':');
    set(groot, 'DefaultAxesGridAlpha',        0.4);
    set(groot, 'DefaultLineLineWidth',        1.5);
    set(groot, 'DefaultLegendBox',            'off');
    if strcmpi(mode, 'dark')
        fg = [0.910 0.902 0.890]; bg = [0.082 0.090 0.110];
        set(groot, 'DefaultFigureColor',      bg);
        set(groot, 'DefaultAxesColor',        bg);
        set(groot, 'DefaultAxesXColor',       fg);
        set(groot, 'DefaultAxesYColor',       fg);
        set(groot, 'DefaultAxesZColor',       fg);
        set(groot, 'DefaultTextColor',        fg);
        set(groot, 'DefaultAxesGridColor',    [0.29 0.31 0.35]);
        set(groot, 'DefaultLegendTextColor',  fg);
        set(groot, 'DefaultLegendColor',      bg);
    else
        set(groot, 'DefaultFigureColor',      'w');
    end
end
