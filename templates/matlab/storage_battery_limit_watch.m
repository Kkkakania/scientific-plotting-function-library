function fig = storage_battery_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 2402, 'storage and battery analysis: control limit watch', 'storage and battery analysis', 'control limit watch');
end
