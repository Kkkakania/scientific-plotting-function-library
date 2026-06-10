function fig = lift_curve()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(13);
    n = 1000; scores = rand(n,1);
    y = rand(n,1) < scores*0.8;
    [~, idx] = sort(-scores); y = y(idx);
    pct = (1:n)/n*100;
    gain = cumsum(y)/sum(y)*100;
    fig = figure;
    plot(pct, gain, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    plot([0 100], [0 100], '--', 'Color', [0.5 0.5 0.5]);
    xlabel('population (%)'); ylabel('cumulative gain (%)');
    title('Lift / Gain curve'); legend({'model','random'}); grid on;
end
