function fig = pareto_front()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    n = 400; f1 = rand(n,1); f2 = (1 - f1.^0.5) + 0.15*rand(n,1);
    pareto = true(n,1);
    for i = 1:n
        for j = 1:n
            if i ~= j && f1(j) <= f1(i) && f2(j) <= f2(i) && (f1(j) < f1(i) || f2(j) < f2(i))
                pareto(i) = false; break;
            end
        end
    end
    fig = figure;
    scatter(f1(~pareto), f2(~pareto), 15, [0.75 0.75 0.75], 'filled'); hold on;
    [fps, idx] = sort(f1(pareto)); f2p = f2(pareto); f2p = f2p(idx);
    plot(fps, f2p, 'Color', palette('cat',2), 'LineWidth', 0.8);
    scatter(fps, f2p, 30, palette('cat',2), 'filled', 'MarkerEdgeColor','k');
    xlabel('objective 1'); ylabel('objective 2'); title('Pareto front');
    legend({'dominated','front line','Pareto front'}); grid on;
end
