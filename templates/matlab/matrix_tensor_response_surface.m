function fig = matrix_tensor_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 4404, 'matrix and tensor visualization: response contour surface', 'matrix and tensor visualization', 'response contour surface');
end
