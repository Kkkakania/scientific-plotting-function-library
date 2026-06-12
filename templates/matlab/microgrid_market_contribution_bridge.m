function fig = microgrid_market_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3808, 'microgrid and market analysis: contribution waterfall', 'microgrid and market analysis', 'contribution waterfall');
end
