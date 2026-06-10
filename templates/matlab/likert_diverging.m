function fig = likert_diverging()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(2);
    questions = arrayfun(@(i)sprintf('Q%d',i), 1:6, 'UniformOutput', false);
    M = 5 + 20*rand(6, 5); M = M ./ sum(M, 2) * 100;
    cols = [palette('cat',2); palette('cat',8); 0.74*[1 1 1]; palette('cat',6); palette('cat',1)];
    fig = figure('Position',[100 100 800 400]); hold on;
    left = -(M(:, 1) + M(:, 2) + M(:, 3)/2);
    for k = 1:5
        for q = 1:6
            rectangle('Position', [left(q), q-0.4, M(q, k), 0.8], 'FaceColor', cols(k, :), 'EdgeColor','w');
        end
        left = left + M(:, k);
    end
    xline(0, 'k');
    set(gca,'YTick',1:6,'YTickLabel',questions);
    xlabel('% respondents'); title('Likert diverging bars');
end
