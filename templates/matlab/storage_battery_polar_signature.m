function fig = storage_battery_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2410, 'storage and battery analysis: polar signature', 'storage and battery analysis', 'polar signature');
end
