function fig = matrix_tensor_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 4410, 'matrix and tensor visualization: polar signature', 'matrix and tensor visualization', 'polar signature');
end
