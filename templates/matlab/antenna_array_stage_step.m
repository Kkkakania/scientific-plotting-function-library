function fig = antenna_array_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 4217, 'antenna array analysis: stage step curve', 'antenna array analysis', 'stage step curve');
end
