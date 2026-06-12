function fig = matrix_tensor_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 4401, 'matrix and tensor visualization: monitoring band time series', 'matrix and tensor visualization', 'monitoring band time series');
end
