function fig = radar_advanced_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 4103, 'advanced radar analysis: state heatmap', 'advanced radar analysis', 'state heatmap');
end
