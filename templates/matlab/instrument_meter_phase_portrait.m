function fig = instrument_meter_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2811, 'instrument and metering: phase portrait', 'instrument and metering', 'phase portrait');
end
