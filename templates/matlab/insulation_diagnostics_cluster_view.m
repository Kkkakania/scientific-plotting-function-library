function fig = insulation_diagnostics_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3905, 'insulation diagnostics: state cluster scatter', 'insulation diagnostics', 'state cluster scatter');
end
