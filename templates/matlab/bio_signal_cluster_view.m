function fig = bio_signal_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2705, 'biomedical signal analysis: state cluster scatter', 'biomedical signal analysis', 'state cluster scatter');
end
