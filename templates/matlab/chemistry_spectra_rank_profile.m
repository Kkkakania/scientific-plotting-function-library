function fig = chemistry_spectra_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 1906, 'chemistry spectra: ranked metric profile', 'chemistry spectra', 'ranked metric profile');
end
