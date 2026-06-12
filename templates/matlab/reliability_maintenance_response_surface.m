function fig = reliability_maintenance_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3304, 'reliability and maintenance: response contour surface', 'reliability and maintenance', 'response contour surface');
end
