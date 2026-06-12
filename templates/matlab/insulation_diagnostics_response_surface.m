function fig = insulation_diagnostics_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3904, 'insulation diagnostics: response contour surface', 'insulation diagnostics', 'response contour surface');
end
