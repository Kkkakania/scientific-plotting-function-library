function fig = chemistry_spectra_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 1915, 'chemistry spectra: interval forest', 'chemistry spectra', 'interval forest');
end
