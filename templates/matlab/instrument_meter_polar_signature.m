function fig = instrument_meter_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2810, 'instrument and metering: polar signature', 'instrument and metering', 'polar signature');
end
