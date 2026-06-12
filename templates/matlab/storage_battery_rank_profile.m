function fig = storage_battery_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2406, 'storage and battery analysis: ranked metric profile', 'storage and battery analysis', 'ranked metric profile');
end
