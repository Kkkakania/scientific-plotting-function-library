function fig = antenna_array_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 4213, 'antenna array analysis: interaction bubble matrix', 'antenna array analysis', 'interaction bubble matrix');
end
