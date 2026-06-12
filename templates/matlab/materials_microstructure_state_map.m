function fig = materials_microstructure_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 1803, 'materials microstructure: state heatmap', 'materials microstructure', 'state heatmap');
end
