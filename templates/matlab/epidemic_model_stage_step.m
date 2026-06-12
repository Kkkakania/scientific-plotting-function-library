function fig = epidemic_model_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3517, 'epidemic dynamics: stage step curve', 'epidemic dynamics', 'stage step curve');
end
