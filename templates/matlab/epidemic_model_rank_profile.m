function fig = epidemic_model_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3506, 'epidemic dynamics: ranked metric profile', 'epidemic dynamics', 'ranked metric profile');
end
