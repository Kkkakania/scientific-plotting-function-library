function fig = geoscience_grid_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 4506, 'geoscience grid analysis: ranked metric profile', 'geoscience grid analysis', 'ranked metric profile');
end
