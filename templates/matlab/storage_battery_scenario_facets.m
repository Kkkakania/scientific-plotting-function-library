function fig = storage_battery_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 2409, 'storage and battery analysis: scenario small multiples', 'storage and battery analysis', 'scenario small multiples');
end
