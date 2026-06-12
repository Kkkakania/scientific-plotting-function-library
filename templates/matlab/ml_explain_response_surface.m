function fig = ml_explain_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 1404, 'machine learning explainability: response contour surface', 'machine learning explainability', 'response contour surface');
end
