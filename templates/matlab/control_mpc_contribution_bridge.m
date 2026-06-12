function fig = control_mpc_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 1608, 'advanced MPC control: contribution waterfall', 'advanced MPC control', 'contribution waterfall');
end
