function fig = seasonal_subseries()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(17);
    months = {'Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'};
    nY = 5;
    M = zeros(nY, 12);
    for y = 1:nY
        season = 5 + 3*sin((0:11)*pi/6);
        M(y, :) = season + (y-1)*0.4 + 0.3*randn(1, 12);
    end
    fig = figure('Position',[100 100 800 400]); hold on;
    for m = 1:12
        xs = m + linspace(-0.3, 0.3, nY);
        plot(xs, M(:, m), '-o', 'Color', palette('cat',1), 'MarkerSize', 3);
        plot([m-0.35 m+0.35], [mean(M(:,m)) mean(M(:,m))], 'Color', palette('cat',2), 'LineWidth', 1.5);
    end
    set(gca,'XTick',1:12,'XTickLabel',months);
    ylabel('value'); title('Seasonal subseries'); grid on;
end
