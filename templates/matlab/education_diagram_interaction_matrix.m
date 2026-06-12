function fig = education_diagram_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3213, 'educational diagramming: interaction bubble matrix', 'educational diagramming', 'interaction bubble matrix');
end
