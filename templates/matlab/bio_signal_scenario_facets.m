function fig = bio_signal_scenario_facets()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('small_multiples', 2709, 'biomedical signal analysis: scenario small multiples', 'biomedical signal analysis', 'scenario small multiples');
end
