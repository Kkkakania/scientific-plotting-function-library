function fig = matrix_tensor_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 4403, 'matrix and tensor visualization: state heatmap', 'matrix and tensor visualization', 'state heatmap');
end
