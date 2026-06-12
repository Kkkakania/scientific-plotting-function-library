function fig = paper_multipanel_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2204, 'paper multipanel layout: response contour surface', 'paper multipanel layout', 'response contour surface');
end
