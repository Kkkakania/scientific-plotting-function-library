function fig = control_mpc_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 1602, 'advanced MPC control: control limit watch', 'advanced MPC control', 'control limit watch');
end
