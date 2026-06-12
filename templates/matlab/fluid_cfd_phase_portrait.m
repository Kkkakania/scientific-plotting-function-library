function fig = fluid_cfd_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2611, 'fluid and CFD analysis: phase portrait', 'fluid and CFD analysis', 'phase portrait');
end
