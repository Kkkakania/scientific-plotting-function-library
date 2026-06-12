function fig = motor_deep_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2317, 'electric motor analysis: stage step curve', 'electric motor analysis', 'stage step curve');
end
