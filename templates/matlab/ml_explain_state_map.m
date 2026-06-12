function fig = ml_explain_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 1403, 'machine learning explainability: state heatmap', 'machine learning explainability', 'state heatmap');
end
