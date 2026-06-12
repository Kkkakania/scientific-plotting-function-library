function fig = chemistry_spectra_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 1916, 'chemistry spectra: composition stream', 'chemistry spectra', 'composition stream');
end
