function fig = quantum_semiconductor_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3004, 'quantum and semiconductor analysis: response contour surface', 'quantum and semiconductor analysis', 'response contour surface');
end
