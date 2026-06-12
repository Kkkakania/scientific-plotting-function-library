function fig = control_mpc_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 1617, 'advanced MPC control: stage step curve', 'advanced MPC control', 'stage step curve');
end
