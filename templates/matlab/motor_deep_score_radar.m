function fig = motor_deep_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2307, 'electric motor analysis: multi-metric radar', 'electric motor analysis', 'multi-metric radar');
end
