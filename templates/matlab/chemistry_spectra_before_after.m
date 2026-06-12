function fig = chemistry_spectra_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 1920, 'chemistry spectra: before-after slope', 'chemistry spectra', 'before-after slope');
end
