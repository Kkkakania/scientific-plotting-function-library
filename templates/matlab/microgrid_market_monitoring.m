function fig = microgrid_market_monitoring()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('band_timeseries', 3801, 'microgrid and market analysis: monitoring band time series', 'microgrid and market analysis', 'monitoring band time series');
end
