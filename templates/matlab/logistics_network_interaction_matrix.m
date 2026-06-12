function fig = logistics_network_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3413, 'logistics and network analysis: interaction bubble matrix', 'logistics and network analysis', 'interaction bubble matrix');
end
