function fig = storage_battery_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2420, 'storage and battery analysis: before-after slope', 'storage and battery analysis', 'before-after slope');
end
