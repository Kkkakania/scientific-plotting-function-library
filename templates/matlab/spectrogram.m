function fig = spectrogram_demo()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    fs = 2000; t = 0:1/fs:2-1/fs;
    sig = chirp(t, 20, 2, 400, 'linear');
    fig = figure('Position',[100 100 800 400]);
    spectrogram(sig, 256, 200, 256, fs, 'yaxis');
    colormap(hot); title('Spectrogram');
end
