function fig = education_diagram_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3201, 'educational diagramming: monitoring band time series', 'educational diagramming', 'monitoring band time series');
end
