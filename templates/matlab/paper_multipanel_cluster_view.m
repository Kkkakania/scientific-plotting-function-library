function fig = paper_multipanel_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2205, 'paper multipanel layout: state cluster scatter', 'paper multipanel layout', 'state cluster scatter');
end
