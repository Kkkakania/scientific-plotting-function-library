function fig = control_mpc_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 1607, 'advanced MPC control: multi-metric radar', 'advanced MPC control', 'multi-metric radar');
end
