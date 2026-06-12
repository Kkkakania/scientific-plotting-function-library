function fig = paper_multipanel_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2213, 'paper multipanel layout: interaction bubble matrix', 'paper multipanel layout', 'interaction bubble matrix');
end
