function fig = chemistry_spectra_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 1901, 'chemistry spectra: monitoring band time series', 'chemistry spectra', 'monitoring band time series');
end
