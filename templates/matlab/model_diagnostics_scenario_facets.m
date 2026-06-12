function fig = model_diagnostics_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 1509, 'model diagnostics: scenario small multiples', 'model diagnostics', 'scenario small multiples');
end
