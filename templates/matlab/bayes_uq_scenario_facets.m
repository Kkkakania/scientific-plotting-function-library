function fig = bayes_uq_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 4309, 'Bayesian uncertainty quantification: scenario small multiples', 'Bayesian uncertainty quantification', 'scenario small multiples');
end
