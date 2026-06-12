function fig = physics_field_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2013, 'physics field analysis: interaction bubble matrix', 'physics field analysis', 'interaction bubble matrix');
end
