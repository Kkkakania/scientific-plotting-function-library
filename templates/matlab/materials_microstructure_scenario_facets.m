function fig = materials_microstructure_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 1809, 'materials microstructure: scenario small multiples', 'materials microstructure', 'scenario small multiples');
end
