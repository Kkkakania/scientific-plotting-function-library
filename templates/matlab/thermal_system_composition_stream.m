function fig = thermal_system_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 2516, 'thermal system analysis: composition stream', 'thermal system analysis', 'composition stream');
end
