function fig = ml_explain_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 1420, 'machine learning explainability: before-after slope', 'machine learning explainability', 'before-after slope');
end
