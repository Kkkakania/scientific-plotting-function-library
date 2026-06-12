function fig = quantum_semiconductor_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3005, 'quantum and semiconductor analysis: state cluster scatter', 'quantum and semiconductor analysis', 'state cluster scatter');
end
