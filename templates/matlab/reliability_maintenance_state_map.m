function fig = reliability_maintenance_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3303, 'reliability and maintenance: state heatmap', 'reliability and maintenance', 'state heatmap');
end
