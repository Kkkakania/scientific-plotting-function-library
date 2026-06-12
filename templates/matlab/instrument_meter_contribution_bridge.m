function fig = instrument_meter_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2808, 'instrument and metering: contribution waterfall', 'instrument and metering', 'contribution waterfall');
end
