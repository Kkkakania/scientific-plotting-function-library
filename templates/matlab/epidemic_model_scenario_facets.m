function fig = epidemic_model_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 3509, 'epidemic dynamics: scenario small multiples', 'epidemic dynamics', 'scenario small multiples');
end
