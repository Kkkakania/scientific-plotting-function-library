function fig = bio_signal_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2710, 'biomedical signal analysis: polar signature', 'biomedical signal analysis', 'polar signature');
end
