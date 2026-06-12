function fig = control_mpc_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 1615, 'advanced MPC control: interval forest', 'advanced MPC control', 'interval forest');
end
