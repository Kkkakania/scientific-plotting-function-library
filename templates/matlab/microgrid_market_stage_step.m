function fig = microgrid_market_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3817, 'microgrid and market analysis: stage step curve', 'microgrid and market analysis', 'stage step curve');
end
