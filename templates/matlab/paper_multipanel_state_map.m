function fig = paper_multipanel_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2203, 'paper multipanel layout: state heatmap', 'paper multipanel layout', 'state heatmap');
end
