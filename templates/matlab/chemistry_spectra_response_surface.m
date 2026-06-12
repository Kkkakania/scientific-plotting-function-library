function fig = chemistry_spectra_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 1904, 'chemistry spectra: response contour surface', 'chemistry spectra', 'response contour surface');
end
