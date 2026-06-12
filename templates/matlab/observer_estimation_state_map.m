function fig = observer_estimation_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 1703, 'observer and state estimation: state heatmap', 'observer and state estimation', 'state heatmap');
end
