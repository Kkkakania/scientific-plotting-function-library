function fig = insulation_diagnostics_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3913, 'insulation diagnostics: interaction bubble matrix', 'insulation diagnostics', 'interaction bubble matrix');
end
