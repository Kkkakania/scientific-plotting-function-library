function fig = optimization_viz_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2903, 'optimization visualization: state heatmap', 'optimization visualization', 'state heatmap');
end
