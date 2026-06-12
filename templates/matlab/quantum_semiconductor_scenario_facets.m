function fig = quantum_semiconductor_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 3009, 'quantum and semiconductor analysis: scenario small multiples', 'quantum and semiconductor analysis', 'scenario small multiples');
end
