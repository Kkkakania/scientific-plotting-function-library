function fig = synthetic_geo_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2106, 'synthetic geospatial grid: ranked metric profile', 'synthetic geospatial grid', 'ranked metric profile');
end
