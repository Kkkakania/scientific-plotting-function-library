function fig = antenna_array_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 4203, 'antenna array analysis: state heatmap', 'antenna array analysis', 'state heatmap');
end
