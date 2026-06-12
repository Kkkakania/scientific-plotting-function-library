function fig = motor_deep_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2306, 'electric motor analysis: ranked metric profile', 'electric motor analysis', 'ranked metric profile');
end
