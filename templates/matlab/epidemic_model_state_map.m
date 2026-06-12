function fig = epidemic_model_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3503, 'epidemic dynamics: state heatmap', 'epidemic dynamics', 'state heatmap');
end
