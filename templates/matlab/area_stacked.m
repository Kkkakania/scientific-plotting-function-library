function fig = area_stacked()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    x = linspace(0, 10, 60);
    Y = abs(2 + 0.5*randn(4, 60) + (1:4)'*0.2);
    fig = figure('Position',[100 100 800 400]);
    h = area(x, Y'); hold on;
    for k = 1:numel(h), h(k).FaceColor = palette('cat',k); h(k).FaceAlpha = 0.8; end
    xlabel('x'); ylabel('value'); title('Stacked area');
    legend(arrayfun(@(i)sprintf('comp %d',i),1:4,'UniformOutput',false));
    grid on;
end
