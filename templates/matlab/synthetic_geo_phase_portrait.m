function fig = synthetic_geo_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2111, 'synthetic geospatial grid: phase portrait', 'synthetic geospatial grid', 'phase portrait');
end
