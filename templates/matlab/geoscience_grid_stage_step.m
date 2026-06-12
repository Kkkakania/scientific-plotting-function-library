function fig = geoscience_grid_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 4517, 'geoscience grid analysis: stage step curve', 'geoscience grid analysis', 'stage step curve');
end
