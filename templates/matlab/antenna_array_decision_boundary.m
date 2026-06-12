function fig = antenna_array_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 4221, 'antenna array analysis: decision boundary', 'antenna array analysis', 'decision boundary');
end
