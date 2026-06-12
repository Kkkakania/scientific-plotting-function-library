function fig = motor_deep_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2303, 'electric motor analysis: state heatmap', 'electric motor analysis', 'state heatmap');
end
