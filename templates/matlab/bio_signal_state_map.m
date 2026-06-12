function fig = bio_signal_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2703, 'biomedical signal analysis: state heatmap', 'biomedical signal analysis', 'state heatmap');
end
