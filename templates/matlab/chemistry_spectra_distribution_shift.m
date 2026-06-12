function fig = chemistry_spectra_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 1912, 'chemistry spectra: distribution shift', 'chemistry spectra', 'distribution shift');
end
