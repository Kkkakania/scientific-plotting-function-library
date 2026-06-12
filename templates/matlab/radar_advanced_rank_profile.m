function fig = radar_advanced_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 4106, 'advanced radar analysis: ranked metric profile', 'advanced radar analysis', 'ranked metric profile');
end
