function fig = motor_deep_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2313, 'electric motor analysis: interaction bubble matrix', 'electric motor analysis', 'interaction bubble matrix');
end
