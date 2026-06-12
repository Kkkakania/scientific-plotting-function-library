function fig = materials_microstructure_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 1801, 'materials microstructure: monitoring band time series', 'materials microstructure', 'monitoring band time series');
end
