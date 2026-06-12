function fig = fluid_cfd_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2605, 'fluid and CFD analysis: state cluster scatter', 'fluid and CFD analysis', 'state cluster scatter');
end
