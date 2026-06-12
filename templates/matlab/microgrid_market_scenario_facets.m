function fig = microgrid_market_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 3809, 'microgrid and market analysis: scenario small multiples', 'microgrid and market analysis', 'scenario small multiples');
end
