function fig = motor_deep_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2304, 'electric motor analysis: response contour surface', 'electric motor analysis', 'response contour surface');
end
