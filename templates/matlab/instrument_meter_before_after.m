function fig = instrument_meter_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2820, 'instrument and metering: before-after slope', 'instrument and metering', 'before-after slope');
end
