function fig = control_mpc_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 1613, 'advanced MPC control: interaction bubble matrix', 'advanced MPC control', 'interaction bubble matrix');
end
