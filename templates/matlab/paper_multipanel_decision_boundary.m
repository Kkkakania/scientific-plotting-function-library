function fig = paper_multipanel_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 2221, 'paper multipanel layout: decision boundary', 'paper multipanel layout', 'decision boundary');
end
