function fig = synthetic_geo_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2113, 'synthetic geospatial grid: interaction bubble matrix', 'synthetic geospatial grid', 'interaction bubble matrix');
end
