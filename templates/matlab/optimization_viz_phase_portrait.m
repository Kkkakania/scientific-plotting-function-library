function fig = optimization_viz_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2911, 'optimization visualization: phase portrait', 'optimization visualization', 'phase portrait');
end
