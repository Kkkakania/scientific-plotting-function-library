function fig = ml_explain_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 1406, 'machine learning explainability: ranked metric profile', 'machine learning explainability', 'ranked metric profile');
end
