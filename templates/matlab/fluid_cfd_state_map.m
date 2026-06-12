function fig = fluid_cfd_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 2603, 'fluid and CFD analysis: state heatmap', 'fluid and CFD analysis', 'state heatmap');
end
