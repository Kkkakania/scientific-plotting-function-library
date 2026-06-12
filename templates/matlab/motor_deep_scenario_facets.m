function fig = motor_deep_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 2309, 'electric motor analysis: scenario small multiples', 'electric motor analysis', 'scenario small multiples');
end
