function fig = instrument_meter_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 2816, 'instrument and metering: composition stream', 'instrument and metering', 'composition stream');
end
