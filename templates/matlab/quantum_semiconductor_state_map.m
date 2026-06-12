function fig = quantum_semiconductor_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3003, 'quantum and semiconductor analysis: state heatmap', 'quantum and semiconductor analysis', 'state heatmap');
end
