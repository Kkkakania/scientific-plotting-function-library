function fig = storage_battery_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 2415, 'storage and battery analysis: interval forest', 'storage and battery analysis', 'interval forest');
end
