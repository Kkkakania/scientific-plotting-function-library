function fig = antenna_array_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 4205, 'antenna array analysis: state cluster scatter', 'antenna array analysis', 'state cluster scatter');
end
