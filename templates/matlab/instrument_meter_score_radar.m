function fig = instrument_meter_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2807, 'instrument and metering: multi-metric radar', 'instrument and metering', 'multi-metric radar');
end
