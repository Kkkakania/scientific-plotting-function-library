function fig = physics_field_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2011, 'physics field analysis: phase portrait', 'physics field analysis', 'phase portrait');
end
