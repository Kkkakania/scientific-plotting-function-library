function fig = protection_fault_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 4005, 'protection and fault analysis: state cluster scatter', 'protection and fault analysis', 'state cluster scatter');
end
