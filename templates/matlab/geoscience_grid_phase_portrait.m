function fig = geoscience_grid_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 4511, 'geoscience grid analysis: phase portrait', 'geoscience grid analysis', 'phase portrait');
end
