function fig = antenna_array_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 4206, 'antenna array analysis: ranked metric profile', 'antenna array analysis', 'ranked metric profile');
end
