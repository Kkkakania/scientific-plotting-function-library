function fig = matrix_tensor_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 4406, 'matrix and tensor visualization: ranked metric profile', 'matrix and tensor visualization', 'ranked metric profile');
end
