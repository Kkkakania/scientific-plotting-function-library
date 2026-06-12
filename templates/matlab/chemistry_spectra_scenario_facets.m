function fig = chemistry_spectra_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 1909, 'chemistry spectra: scenario small multiples', 'chemistry spectra', 'scenario small multiples');
end
