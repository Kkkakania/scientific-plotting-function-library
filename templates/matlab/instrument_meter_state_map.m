function fig = instrument_meter_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2803, 'instrument and metering: state heatmap', 'instrument and metering', 'state heatmap');
end
