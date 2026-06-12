function fig = instrument_meter_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2805, 'instrument and metering: state cluster scatter', 'instrument and metering', 'state cluster scatter');
end
