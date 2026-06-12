function fig = power_system_deep_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3606, 'power system analysis: ranked metric profile', 'power system analysis', 'ranked metric profile');
end
