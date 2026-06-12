function fig = synthetic_geo_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 2121, 'synthetic geospatial grid: decision boundary', 'synthetic geospatial grid', 'decision boundary');
end
