function fig = epidemic_model_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 3521, 'epidemic dynamics: decision boundary', 'epidemic dynamics', 'decision boundary');
end
