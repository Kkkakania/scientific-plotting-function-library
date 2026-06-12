function fig = synthetic_geo_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2103, 'synthetic geospatial grid: state heatmap', 'synthetic geospatial grid', 'state heatmap');
end
