function fig = thermal_system_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2506, 'thermal system analysis: ranked metric profile', 'thermal system analysis', 'ranked metric profile');
end
