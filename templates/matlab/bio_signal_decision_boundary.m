function fig = bio_signal_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 2721, 'biomedical signal analysis: decision boundary', 'biomedical signal analysis', 'decision boundary');
end
