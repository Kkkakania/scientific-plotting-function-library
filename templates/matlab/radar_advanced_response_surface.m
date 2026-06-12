function fig = radar_advanced_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 4104, 'advanced radar analysis: response contour surface', 'advanced radar analysis', 'response contour surface');
end
