function fig = acoustic_voice_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 3121, 'acoustic and voice analysis: decision boundary', 'acoustic and voice analysis', 'decision boundary');
end
