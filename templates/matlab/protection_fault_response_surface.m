function fig = protection_fault_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 4004, 'protection and fault analysis: response contour surface', 'protection and fault analysis', 'response contour surface');
end
