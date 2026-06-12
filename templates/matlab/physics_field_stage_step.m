function fig = physics_field_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2017, 'physics field analysis: stage step curve', 'physics field analysis', 'stage step curve');
end
