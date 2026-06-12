function fig = materials_microstructure_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 1805, 'materials microstructure: state cluster scatter', 'materials microstructure', 'state cluster scatter');
end
