function fig = microgrid_market_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3806, 'microgrid and market analysis: ranked metric profile', 'microgrid and market analysis', 'ranked metric profile');
end
