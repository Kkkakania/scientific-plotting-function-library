function fig = model_diagnostics_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 1517, 'model diagnostics: stage step curve', 'model diagnostics', 'stage step curve');
end
