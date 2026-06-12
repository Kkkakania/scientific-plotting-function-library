function fig = control_mpc_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 1612, 'advanced MPC control: distribution shift', 'advanced MPC control', 'distribution shift');
end
