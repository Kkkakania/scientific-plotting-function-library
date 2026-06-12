function fig = ml_explain_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 1415, 'machine learning explainability: interval forest', 'machine learning explainability', 'interval forest');
end
