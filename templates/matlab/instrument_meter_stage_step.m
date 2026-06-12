function fig = instrument_meter_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2817, 'instrument and metering: stage step curve', 'instrument and metering', 'stage step curve');
end
