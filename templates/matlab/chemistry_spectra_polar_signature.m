function fig = chemistry_spectra_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 1910, 'chemistry spectra: polar signature', 'chemistry spectra', 'polar signature');
end
