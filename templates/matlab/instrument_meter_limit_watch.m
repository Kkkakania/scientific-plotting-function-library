function fig = instrument_meter_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 2802, 'instrument and metering: control limit watch', 'instrument and metering', 'control limit watch');
end
