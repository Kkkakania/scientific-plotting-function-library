function fig = bio_signal_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 2716, 'biomedical signal analysis: composition stream', 'biomedical signal analysis', 'composition stream');
end
