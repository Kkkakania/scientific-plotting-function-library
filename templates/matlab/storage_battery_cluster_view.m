function fig = storage_battery_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2405, 'storage and battery analysis: state cluster scatter', 'storage and battery analysis', 'state cluster scatter');
end
