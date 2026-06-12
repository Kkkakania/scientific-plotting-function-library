function fig = education_diagram_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3211, 'educational diagramming: phase portrait', 'educational diagramming', 'phase portrait');
end
