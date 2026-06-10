function fig = small_multiples()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4);
    t = linspace(0, 10, 100);
    fig = figure('Position',[100 100 900 500]);
    for i = 1:8
        subplot(2, 4, i);
        y = sin(t + (i-1)*0.5) .* exp(-t/(5+i)) + 0.05*randn(size(t));
        plot(t, y, 'Color', palette('cat',i));
        title(sprintf('series %d', i), 'FontSize', 9); grid on;
        if i > 4, xlabel('t'); end
        if mod(i-1, 4) == 0, ylabel('y'); end
    end
    sgtitle('Small multiples');
end
