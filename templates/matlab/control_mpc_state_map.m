function fig = control_mpc_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 1603, 'advanced MPC control: state heatmap', 'advanced MPC control', 'state heatmap');
end
