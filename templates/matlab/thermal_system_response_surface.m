function fig = thermal_system_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2504, 'thermal system analysis: response contour surface', 'thermal system analysis', 'response contour surface');
end
