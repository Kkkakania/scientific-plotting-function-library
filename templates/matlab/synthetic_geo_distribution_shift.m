function fig = synthetic_geo_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 2112, 'synthetic geospatial grid: distribution shift', 'synthetic geospatial grid', 'distribution shift');
end
