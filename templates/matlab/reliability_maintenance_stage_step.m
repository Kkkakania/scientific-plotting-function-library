function fig = reliability_maintenance_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3317, 'reliability and maintenance: stage step curve', 'reliability and maintenance', 'stage step curve');
end
