function fig = control_mpc_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 1605, 'advanced MPC control: state cluster scatter', 'advanced MPC control', 'state cluster scatter');
end
