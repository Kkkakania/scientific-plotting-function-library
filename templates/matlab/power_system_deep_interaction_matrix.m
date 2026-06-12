function fig = power_system_deep_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3613, 'power system analysis: interaction bubble matrix', 'power system analysis', 'interaction bubble matrix');
end
