function fig = thermal_system_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2503, 'thermal system analysis: state heatmap', 'thermal system analysis', 'state heatmap');
end
