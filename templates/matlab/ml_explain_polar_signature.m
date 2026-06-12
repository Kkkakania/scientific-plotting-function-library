function fig = ml_explain_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 1410, 'machine learning explainability: polar signature', 'machine learning explainability', 'polar signature');
end
