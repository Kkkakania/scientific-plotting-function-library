function fig = acoustic_voice_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3105, 'acoustic and voice analysis: state cluster scatter', 'acoustic and voice analysis', 'state cluster scatter');
end
