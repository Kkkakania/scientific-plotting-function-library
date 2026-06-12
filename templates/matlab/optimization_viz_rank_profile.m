function fig = optimization_viz_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2906, 'optimization visualization: ranked metric profile', 'optimization visualization', 'ranked metric profile');
end
