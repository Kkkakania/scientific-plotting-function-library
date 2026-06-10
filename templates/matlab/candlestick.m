function fig = candlestick()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(20);
    n = 30;
    closep = 100 + cumsum(randn(1, n));
    openp = closep + randn(1, n);
    highp = max(openp, closep) + 1.5*rand(1, n);
    lowp  = min(openp, closep) - 1.5*rand(1, n);
    fig = figure('Position',[100 100 800 400]); hold on;
    for i = 1:n
        if closep(i) >= openp(i), c = [0.15 0.65 0.60]; else, c = [0.94 0.32 0.31]; end
        plot([i i], [lowp(i) highp(i)], 'k', 'LineWidth', 0.7);
        rectangle('Position',[i-0.3, min(openp(i),closep(i)), 0.6, abs(closep(i)-openp(i))], ...
                  'FaceColor', c, 'EdgeColor','none');
    end
    xlim([0 n+1]); xlabel('day'); ylabel('price'); title('Candlestick'); grid on;
end
