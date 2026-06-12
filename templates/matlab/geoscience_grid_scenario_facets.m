function fig = geoscience_grid_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 4509, 'geoscience grid analysis: scenario small multiples', 'geoscience grid analysis', 'scenario small multiples');
end
