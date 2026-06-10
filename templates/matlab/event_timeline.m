function fig = event_timeline()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(19);
    cats = {'build','test','deploy','rollback'};
    fig = figure('Position',[100 100 800 350]); hold on;
    for i = 1:numel(cats)
        times = sort(100*rand(1, 6));
        plot(times, ones(size(times))*i, 'o', 'Color', palette('cat',i), ...
             'MarkerFaceColor', palette('cat',i), 'MarkerSize', 10);
    end
    set(gca,'YTick',1:numel(cats),'YTickLabel',cats);
    xlabel('time'); title('Event timeline'); grid on;
    legend(cats, 'Location','southeast');
end
