function fig = model_diagnostics_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 1503, 'model diagnostics: state heatmap', 'model diagnostics', 'state heatmap');
end
