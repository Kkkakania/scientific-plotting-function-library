function fig = epidemic_model_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3504, 'epidemic dynamics: response contour surface', 'epidemic dynamics', 'response contour surface');
end
