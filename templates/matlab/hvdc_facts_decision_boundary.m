function fig = hvdc_facts_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 3721, 'HVDC and FACTS analysis: decision boundary', 'HVDC and FACTS analysis', 'decision boundary');
end
