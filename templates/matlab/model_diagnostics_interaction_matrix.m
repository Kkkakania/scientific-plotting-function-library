function fig = model_diagnostics_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 1513, 'model diagnostics: interaction bubble matrix', 'model diagnostics', 'interaction bubble matrix');
end
