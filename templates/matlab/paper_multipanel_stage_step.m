function fig = paper_multipanel_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2217, 'paper multipanel layout: stage step curve', 'paper multipanel layout', 'stage step curve');
end
