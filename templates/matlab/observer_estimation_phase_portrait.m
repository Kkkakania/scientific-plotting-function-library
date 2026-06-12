function fig = observer_estimation_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 1711, 'observer and state estimation: phase portrait', 'observer and state estimation', 'phase portrait');
end
