function fig = control_mpc_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 1621, 'advanced MPC control: decision boundary', 'advanced MPC control', 'decision boundary');
end
