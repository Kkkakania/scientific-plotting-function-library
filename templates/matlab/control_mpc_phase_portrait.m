function fig = control_mpc_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 1611, 'advanced MPC control: phase portrait', 'advanced MPC control', 'phase portrait');
end
