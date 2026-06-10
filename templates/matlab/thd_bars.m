function fig = thd_bars()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    loads = {'LED','Motor','PC','Heater','EV','Inverter'};
    thd_v = 2 + 6*rand(1,6); thd_i = 5 + 30*rand(1,6);
    fig = figure;
    bar([thd_v; thd_i]', 'grouped');
    set(gca,'XTickLabel',loads);
    ylabel('THD (%)'); title('THD comparison'); yline(8,'--r','V limit');
    legend({'V THD','I THD'}); grid on;
end
