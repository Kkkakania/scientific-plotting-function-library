function fig = logistics_network_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3403, 'logistics and network analysis: state heatmap', 'logistics and network analysis', 'state heatmap');
end
