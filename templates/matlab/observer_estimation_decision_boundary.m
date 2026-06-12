function fig = observer_estimation_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 1721, 'observer and state estimation: decision boundary', 'observer and state estimation', 'decision boundary');
end
