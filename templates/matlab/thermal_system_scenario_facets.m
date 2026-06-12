function fig = thermal_system_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 2509, 'thermal system analysis: scenario small multiples', 'thermal system analysis', 'scenario small multiples');
end
