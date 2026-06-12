function fig = thermal_system_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2511, 'thermal system analysis: phase portrait', 'thermal system analysis', 'phase portrait');
end
