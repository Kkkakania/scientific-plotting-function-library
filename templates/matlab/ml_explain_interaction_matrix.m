function fig = ml_explain_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 1413, 'machine learning explainability: interaction bubble matrix', 'machine learning explainability', 'interaction bubble matrix');
end
