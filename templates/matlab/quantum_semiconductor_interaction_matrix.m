function fig = quantum_semiconductor_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3013, 'quantum and semiconductor analysis: interaction bubble matrix', 'quantum and semiconductor analysis', 'interaction bubble matrix');
end
