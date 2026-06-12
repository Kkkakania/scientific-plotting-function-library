function fig = acoustic_voice_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3113, 'acoustic and voice analysis: interaction bubble matrix', 'acoustic and voice analysis', 'interaction bubble matrix');
end
