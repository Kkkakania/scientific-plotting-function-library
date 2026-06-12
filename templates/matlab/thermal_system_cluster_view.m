function fig = thermal_system_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2505, 'thermal system analysis: state cluster scatter', 'thermal system analysis', 'state cluster scatter');
end
