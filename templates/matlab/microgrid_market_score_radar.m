function fig = microgrid_market_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3807, 'microgrid and market analysis: multi-metric radar', 'microgrid and market analysis', 'multi-metric radar');
end
