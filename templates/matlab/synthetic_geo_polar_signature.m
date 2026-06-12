function fig = synthetic_geo_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2110, 'synthetic geospatial grid: polar signature', 'synthetic geospatial grid', 'polar signature');
end
