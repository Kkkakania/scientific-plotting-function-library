function fig = storage_battery_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2411, 'storage and battery analysis: phase portrait', 'storage and battery analysis', 'phase portrait');
end
