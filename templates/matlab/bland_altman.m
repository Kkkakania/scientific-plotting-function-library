function fig = bland_altman()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(4); c = palette('cat',1);
    true_v = 20 + 80*rand(80,1);
    m1 = true_v + 2*randn(80,1); m2 = true_v + 0.5 + 2*randn(80,1);
    mn = (m1+m2)/2; dif = m1-m2; md = mean(dif); sd = std(dif);
    fig = figure;
    scatter(mn, dif, 30, c, 'filled', 'MarkerFaceAlpha', 0.7, 'MarkerEdgeColor','w'); hold on;
    yline(md, 'k-');
    yline(md+1.96*sd, '--', 'Color', [0.5 0.5 0.5]);
    yline(md-1.96*sd, '--', 'Color', [0.5 0.5 0.5]);
    xlabel('(M1+M2)/2'); ylabel('M1-M2'); title('Bland-Altman'); grid on;
end
