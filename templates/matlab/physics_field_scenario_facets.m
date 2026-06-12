function fig = physics_field_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 2009, 'physics field analysis: scenario small multiples', 'physics field analysis', 'scenario small multiples');
end
