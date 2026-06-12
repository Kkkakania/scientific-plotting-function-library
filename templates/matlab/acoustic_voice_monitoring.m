function fig = acoustic_voice_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3101, 'acoustic and voice analysis: monitoring band time series', 'acoustic and voice analysis', 'monitoring band time series');
end
