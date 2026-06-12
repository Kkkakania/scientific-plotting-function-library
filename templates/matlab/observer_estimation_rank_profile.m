function fig = observer_estimation_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 1706, 'observer and state estimation: ranked metric profile', 'observer and state estimation', 'ranked metric profile');
end
