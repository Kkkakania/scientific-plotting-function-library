function fig = storage_battery_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2417, 'storage and battery analysis: stage step curve', 'storage and battery analysis', 'stage step curve');
end
