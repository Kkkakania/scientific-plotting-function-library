function fig = physics_field_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2005, 'physics field analysis: state cluster scatter', 'physics field analysis', 'state cluster scatter');
end
