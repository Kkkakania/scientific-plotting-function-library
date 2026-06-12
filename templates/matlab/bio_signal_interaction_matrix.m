function fig = bio_signal_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2713, 'biomedical signal analysis: interaction bubble matrix', 'biomedical signal analysis', 'interaction bubble matrix');
end
