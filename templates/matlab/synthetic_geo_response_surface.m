function fig = synthetic_geo_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2104, 'synthetic geospatial grid: response contour surface', 'synthetic geospatial grid', 'response contour surface');
end
