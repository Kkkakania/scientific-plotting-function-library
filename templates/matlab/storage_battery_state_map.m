function fig = storage_battery_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2403, 'storage and battery analysis: state heatmap', 'storage and battery analysis', 'state heatmap');
end
