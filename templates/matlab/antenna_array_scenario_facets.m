function fig = antenna_array_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 4209, 'antenna array analysis: scenario small multiples', 'antenna array analysis', 'scenario small multiples');
end
