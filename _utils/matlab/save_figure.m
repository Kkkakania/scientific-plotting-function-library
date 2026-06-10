function save_figure(fig, basename, out_dir, formats)
    if nargin < 3 || isempty(out_dir), out_dir = '.'; end
    if nargin < 4 || isempty(formats), formats = {'png'}; end
    if ~exist(out_dir, 'dir'), mkdir(out_dir); end
    for k = 1:numel(formats)
        f = formats{k};
        p = fullfile(out_dir, sprintf('%s.%s', basename, f));
        switch lower(f)
            case 'png', print(fig, p, '-dpng', '-r300');
            case 'svg', print(fig, p, '-dsvg');
            case 'pdf', set(fig, 'PaperPositionMode','auto'); print(fig, p, '-dpdf', '-bestfit');
        end
    end
end
