function fig = paper_multipanel_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2211, 'paper multipanel layout: phase portrait', 'paper multipanel layout', 'phase portrait');
end
