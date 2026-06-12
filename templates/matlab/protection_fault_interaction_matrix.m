function fig = protection_fault_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 4013, 'protection and fault analysis: interaction bubble matrix', 'protection and fault analysis', 'interaction bubble matrix');
end
