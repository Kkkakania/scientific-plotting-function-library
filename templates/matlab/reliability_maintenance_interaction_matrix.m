function fig = reliability_maintenance_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3313, 'reliability and maintenance: interaction bubble matrix', 'reliability and maintenance', 'interaction bubble matrix');
end
