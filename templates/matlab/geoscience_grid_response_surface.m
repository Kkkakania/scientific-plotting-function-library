function fig = geoscience_grid_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 4504, 'geoscience grid analysis: response contour surface', 'geoscience grid analysis', 'response contour surface');
end
