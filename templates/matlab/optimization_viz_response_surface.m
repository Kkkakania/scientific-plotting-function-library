function fig = optimization_viz_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2904, 'optimization visualization: response contour surface', 'optimization visualization', 'response contour surface');
end
