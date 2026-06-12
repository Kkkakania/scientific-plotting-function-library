function fig = model_diagnostics_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 1504, 'model diagnostics: response contour surface', 'model diagnostics', 'response contour surface');
end
