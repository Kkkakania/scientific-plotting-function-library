function fig = thermal_system_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2517, 'thermal system analysis: stage step curve', 'thermal system analysis', 'stage step curve');
end
