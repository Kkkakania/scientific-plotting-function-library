function fig = microgrid_market_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3811, 'microgrid and market analysis: phase portrait', 'microgrid and market analysis', 'phase portrait');
end
