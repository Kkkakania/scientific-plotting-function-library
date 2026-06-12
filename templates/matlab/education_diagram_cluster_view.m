function fig = education_diagram_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3205, 'educational diagramming: state cluster scatter', 'educational diagramming', 'state cluster scatter');
end
