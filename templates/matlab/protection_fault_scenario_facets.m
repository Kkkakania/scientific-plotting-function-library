function fig = protection_fault_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 4009, 'protection and fault analysis: scenario small multiples', 'protection and fault analysis', 'scenario small multiples');
end
