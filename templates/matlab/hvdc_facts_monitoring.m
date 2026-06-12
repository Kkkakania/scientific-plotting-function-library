function fig = hvdc_facts_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3701, 'HVDC and FACTS analysis: monitoring band time series', 'HVDC and FACTS analysis', 'monitoring band time series');
end
