function fig = antenna_array_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 4204, 'antenna array analysis: response contour surface', 'antenna array analysis', 'response contour surface');
end
