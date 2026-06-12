function fig = chemistry_spectra_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 1913, 'chemistry spectra: interaction bubble matrix', 'chemistry spectra', 'interaction bubble matrix');
end
