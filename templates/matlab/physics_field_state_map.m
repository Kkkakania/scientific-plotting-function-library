function fig = physics_field_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2003, 'physics field analysis: state heatmap', 'physics field analysis', 'state heatmap');
end
