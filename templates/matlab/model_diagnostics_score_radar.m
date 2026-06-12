function fig = model_diagnostics_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 1507, 'model diagnostics: multi-metric radar', 'model diagnostics', 'multi-metric radar');
end
