function fig = insulation_diagnostics_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3907, 'insulation diagnostics: multi-metric radar', 'insulation diagnostics', 'multi-metric radar');
end
