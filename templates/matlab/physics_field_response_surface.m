function fig = physics_field_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2004, 'physics field analysis: response contour surface', 'physics field analysis', 'response contour surface');
end
