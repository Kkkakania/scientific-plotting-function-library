function fig = acoustic_voice_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3106, 'acoustic and voice analysis: ranked metric profile', 'acoustic and voice analysis', 'ranked metric profile');
end
