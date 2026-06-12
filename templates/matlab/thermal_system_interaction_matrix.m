function fig = thermal_system_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2513, 'thermal system analysis: interaction bubble matrix', 'thermal system analysis', 'interaction bubble matrix');
end
