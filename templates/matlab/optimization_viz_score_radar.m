function fig = optimization_viz_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2907, 'optimization visualization: multi-metric radar', 'optimization visualization', 'multi-metric radar');
end
