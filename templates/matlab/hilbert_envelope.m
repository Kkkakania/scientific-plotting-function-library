function fig = hilbert_envelope()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 1000; t = 0:1/fs:2-1/fs;
    sig = chirp(t, 20, 2, 150, 'linear');
    analytic = hilbert(sig);
    inst_phase = unwrap(angle(analytic));
    inst_freq = diff(inst_phase) / (2*pi) * fs;
    fig = figure('Position',[100 100 800 400]);
    plot(t(2:end), inst_freq, 'Color', palette('cat',1));
    xlabel('t (s)'); ylabel('instantaneous freq (Hz)');
    title('Instantaneous frequency'); grid on;
end
