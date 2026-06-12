function fig = hvdc_facts_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 3709, 'HVDC and FACTS analysis: scenario small multiples', 'HVDC and FACTS analysis', 'scenario small multiples');
end
