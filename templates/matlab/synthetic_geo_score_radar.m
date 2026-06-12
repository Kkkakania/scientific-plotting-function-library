function fig = synthetic_geo_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2107, 'synthetic geospatial grid: multi-metric radar', 'synthetic geospatial grid', 'multi-metric radar');
end
