function fig = synthetic_geo_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2117, 'synthetic geospatial grid: stage step curve', 'synthetic geospatial grid', 'stage step curve');
end
