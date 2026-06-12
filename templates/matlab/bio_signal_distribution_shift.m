function fig = bio_signal_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 2712, 'biomedical signal analysis: distribution shift', 'biomedical signal analysis', 'distribution shift');
end
