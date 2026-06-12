function fig = control_mpc_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 1620, 'advanced MPC control: before-after slope', 'advanced MPC control', 'before-after slope');
end
