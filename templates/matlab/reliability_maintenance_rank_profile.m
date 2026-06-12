function fig = reliability_maintenance_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3306, 'reliability and maintenance: ranked metric profile', 'reliability and maintenance', 'ranked metric profile');
end
