function fig = power_system_deep_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3611, 'power system analysis: phase portrait', 'power system analysis', 'phase portrait');
end
