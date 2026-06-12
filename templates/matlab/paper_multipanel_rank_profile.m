function fig = paper_multipanel_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2206, 'paper multipanel layout: ranked metric profile', 'paper multipanel layout', 'ranked metric profile');
end
