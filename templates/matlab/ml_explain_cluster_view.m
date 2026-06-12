function fig = ml_explain_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 1405, 'machine learning explainability: state cluster scatter', 'machine learning explainability', 'state cluster scatter');
end
