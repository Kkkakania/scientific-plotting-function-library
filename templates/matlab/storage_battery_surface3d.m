function fig = storage_battery_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 2418, 'storage and battery analysis: 3D response surface', 'storage and battery analysis', '3D response surface');
end
