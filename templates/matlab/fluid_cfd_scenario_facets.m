function fig = fluid_cfd_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 2609, 'fluid and CFD analysis: scenario small multiples', 'fluid and CFD analysis', 'scenario small multiples');
end
