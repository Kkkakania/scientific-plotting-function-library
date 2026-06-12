function fig = model_diagnostics_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 1505, 'model diagnostics: state cluster scatter', 'model diagnostics', 'state cluster scatter');
end
