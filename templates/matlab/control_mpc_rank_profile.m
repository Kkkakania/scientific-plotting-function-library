function fig = control_mpc_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 1606, 'advanced MPC control: ranked metric profile', 'advanced MPC control', 'ranked metric profile');
end
