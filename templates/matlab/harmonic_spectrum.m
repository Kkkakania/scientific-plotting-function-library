function fig = harmonic_spectrum()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    orders = 1:25; amps = zeros(1, 25); amps(1) = 1;
    amps([3 5 7 11]) = [0.3 0.18 0.08 0.05]; amps = amps + 0.02*rand(1, 25);
    fig = figure;
    bar(orders, amps*100, 'FaceColor', palette('cat',1), 'BarWidth', 0.6);
    xlabel('harmonic order'); ylabel('% of fundamental'); title('Harmonic spectrum');
    grid on;
end
