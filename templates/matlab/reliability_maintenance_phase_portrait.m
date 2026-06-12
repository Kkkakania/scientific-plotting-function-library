function fig = reliability_maintenance_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3311, 'reliability and maintenance: phase portrait', 'reliability and maintenance', 'phase portrait');
end
