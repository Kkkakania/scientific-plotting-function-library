function fig = matrix_tensor_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 4408, 'matrix and tensor visualization: contribution waterfall', 'matrix and tensor visualization', 'contribution waterfall');
end
