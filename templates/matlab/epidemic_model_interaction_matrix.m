function fig = epidemic_model_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3513, 'epidemic dynamics: interaction bubble matrix', 'epidemic dynamics', 'interaction bubble matrix');
end
