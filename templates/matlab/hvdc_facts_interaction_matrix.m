function fig = hvdc_facts_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3713, 'HVDC and FACTS analysis: interaction bubble matrix', 'HVDC and FACTS analysis', 'interaction bubble matrix');
end
