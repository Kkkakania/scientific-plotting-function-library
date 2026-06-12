function fig = geoscience_grid_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 4513, 'geoscience grid analysis: interaction bubble matrix', 'geoscience grid analysis', 'interaction bubble matrix');
end
