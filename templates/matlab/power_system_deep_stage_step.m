function fig = power_system_deep_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3617, 'power system analysis: stage step curve', 'power system analysis', 'stage step curve');
end
