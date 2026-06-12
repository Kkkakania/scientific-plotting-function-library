function fig = chemistry_spectra_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 1905, 'chemistry spectra: state cluster scatter', 'chemistry spectra', 'state cluster scatter');
end
