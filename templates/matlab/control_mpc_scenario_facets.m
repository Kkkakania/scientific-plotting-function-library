function fig = control_mpc_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 1609, 'advanced MPC control: scenario small multiples', 'advanced MPC control', 'scenario small multiples');
end
