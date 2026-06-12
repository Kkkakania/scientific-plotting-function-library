function fig = optimization_viz_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2917, 'optimization visualization: stage step curve', 'optimization visualization', 'stage step curve');
end
