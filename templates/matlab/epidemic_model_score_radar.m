function fig = epidemic_model_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3507, 'epidemic dynamics: multi-metric radar', 'epidemic dynamics', 'multi-metric radar');
end
