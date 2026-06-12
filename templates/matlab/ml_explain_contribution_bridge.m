function fig = ml_explain_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 1408, 'machine learning explainability: contribution waterfall', 'machine learning explainability', 'contribution waterfall');
end
