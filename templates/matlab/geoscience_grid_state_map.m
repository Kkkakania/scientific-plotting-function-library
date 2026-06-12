function fig = geoscience_grid_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 4503, 'geoscience grid analysis: state heatmap', 'geoscience grid analysis', 'state heatmap');
end
