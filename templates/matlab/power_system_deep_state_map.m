function fig = power_system_deep_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3603, 'power system analysis: state heatmap', 'power system analysis', 'state heatmap');
end
