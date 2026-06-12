function fig = education_diagram_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3203, 'educational diagramming: state heatmap', 'educational diagramming', 'state heatmap');
end
