function fig = matrix_tensor_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 4405, 'matrix and tensor visualization: state cluster scatter', 'matrix and tensor visualization', 'state cluster scatter');
end
