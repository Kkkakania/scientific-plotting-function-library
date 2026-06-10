function fig = observer_estimate()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    t = linspace(0, 5, 500);
    true_x = sin(2*t).*exp(-0.3*t);
    err = 0.8*exp(-1.5*t);
    est = true_x + err.*cos(5*t);
    fig = figure('Position',[100 100 800 500]);
    subplot(2,1,1);
    plot(t, true_x, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    plot(t, est, '--', 'Color', palette('cat',2), 'LineWidth', 1.5);
    ylabel('state'); title('Observer estimate');
    legend({'true x','estimate'}); grid on;
    subplot(2,1,2);
    plot(t, true_x - est, 'Color', palette('cat',3));
    yline(0, 'Color', [0.5 0.5 0.5]);
    xlabel('t'); ylabel('error'); grid on;
end
