function fig = sensitivity_function()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    w = logspace(-2, 2, 500); s = 1j*w;
    K = 5*(s + 2)./(s + 10); P = 1./(s.*(s+1));
    L = K.*P; S = 1./(1 + L); T = L./(1 + L); KS = K.*S;
    fig = figure;
    semilogx(w, 20*log10(abs(S)),  'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    semilogx(w, 20*log10(abs(T)),  'Color', palette('cat',2), 'LineWidth', 1.5);
    semilogx(w, 20*log10(abs(KS)), 'Color', palette('cat',3), 'LineWidth', 1.5);
    yline(0, 'Color', [0.5 0.5 0.5]);
    xlabel('\omega (rad/s)'); ylabel('magnitude (dB)');
    title('Sensitivity functions'); legend({'|S|','|T|','|KS|'}); grid on;
end
