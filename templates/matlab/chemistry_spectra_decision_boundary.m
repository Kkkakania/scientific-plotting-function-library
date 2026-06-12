function fig = chemistry_spectra_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 1921, 'chemistry spectra: decision boundary', 'chemistry spectra', 'decision boundary');
end
