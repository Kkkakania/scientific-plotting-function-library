function fig = power_system_deep_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 3609, 'power system analysis: scenario small multiples', 'power system analysis', 'scenario small multiples');
end
