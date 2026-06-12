function fig = reliability_maintenance_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 3316, 'reliability and maintenance: composition stream', 'reliability and maintenance', 'composition stream');
end
