function fig = storage_battery_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 2412, 'storage and battery analysis: distribution shift', 'storage and battery analysis', 'distribution shift');
end
