function fig = chemistry_spectra_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 1903, 'chemistry spectra: state heatmap', 'chemistry spectra', 'state heatmap');
end
