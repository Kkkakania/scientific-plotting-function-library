function fig = observer_estimation_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 1713, 'observer and state estimation: interaction bubble matrix', 'observer and state estimation', 'interaction bubble matrix');
end
