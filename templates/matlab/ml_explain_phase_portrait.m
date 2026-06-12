function fig = ml_explain_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 1411, 'machine learning explainability: phase portrait', 'machine learning explainability', 'phase portrait');
end
