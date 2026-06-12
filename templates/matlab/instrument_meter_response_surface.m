function fig = instrument_meter_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2804, 'instrument and metering: response contour surface', 'instrument and metering', 'response contour surface');
end
