function fig = instrument_meter_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 2812, 'instrument and metering: distribution shift', 'instrument and metering', 'distribution shift');
end
