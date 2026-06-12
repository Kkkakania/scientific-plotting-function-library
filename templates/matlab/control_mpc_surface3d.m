function fig = control_mpc_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 1618, 'advanced MPC control: 3D response surface', 'advanced MPC control', '3D response surface');
end
