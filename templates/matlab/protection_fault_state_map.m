function fig = protection_fault_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 4003, 'protection and fault analysis: state heatmap', 'protection and fault analysis', 'state heatmap');
end
