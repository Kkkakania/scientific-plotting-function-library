function fig = control_mpc_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 1610, 'advanced MPC control: polar signature', 'advanced MPC control', 'polar signature');
end
