function fig = bio_signal_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2706, 'biomedical signal analysis: ranked metric profile', 'biomedical signal analysis', 'ranked metric profile');
end
