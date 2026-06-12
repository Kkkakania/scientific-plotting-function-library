function fig = synthetic_geo_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2120, 'synthetic geospatial grid: before-after slope', 'synthetic geospatial grid', 'before-after slope');
end
