function fig = motor_deep_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2311, 'electric motor analysis: phase portrait', 'electric motor analysis', 'phase portrait');
end
