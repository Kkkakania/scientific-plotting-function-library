function fig = observer_estimation_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 1705, 'observer and state estimation: state cluster scatter', 'observer and state estimation', 'state cluster scatter');
end
