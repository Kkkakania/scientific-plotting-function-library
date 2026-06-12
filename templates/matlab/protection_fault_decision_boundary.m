function fig = protection_fault_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 4021, 'protection and fault analysis: decision boundary', 'protection and fault analysis', 'decision boundary');
end
