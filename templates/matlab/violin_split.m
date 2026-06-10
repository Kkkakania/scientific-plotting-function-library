function fig = violin_split()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    fig = figure; hold on;
    for i = 1:4
        l = randn(200,1); r = randn(200,1) + 0.5;
        [fl, xl] = ksdensity(l); fl = fl/max(fl)*0.3;
        [fr, xr] = ksdensity(r); fr = fr/max(fr)*0.3;
        fill([i-fl, i*ones(size(xl))], [xl, fliplr(xl)], palette('cat',1), 'FaceAlpha', 0.6, 'EdgeColor','none');
        fill([i+fr, i*ones(size(xr))], [xr, fliplr(xr)], palette('cat',2), 'FaceAlpha', 0.6, 'EdgeColor','none');
    end
    set(gca,'XTick',1:4,'XTickLabel',{'A','B','C','D'});
    ylabel('value'); title('Split violin');
    legend({'left','right'}); grid on;
end
