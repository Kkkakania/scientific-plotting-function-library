function fig = line_basic()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); c = palette('cat', 1);
    x = linspace(0, 10, 100); y = sin(x);
    fig = figure; plot(x, y, 'Color', c, 'LineWidth', 1.5);
    xlabel('x'); ylabel('y'); title('Line plot'); grid on;
end
