function fig = insulation_diagnostics_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3917, 'insulation diagnostics: stage step curve', 'insulation diagnostics', 'stage step curve');
end
