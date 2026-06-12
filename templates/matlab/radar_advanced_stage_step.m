function fig = radar_advanced_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 4117, 'advanced radar analysis: stage step curve', 'advanced radar analysis', 'stage step curve');
end
