function fig = radar_advanced_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 4111, 'advanced radar analysis: phase portrait', 'advanced radar analysis', 'phase portrait');
end
