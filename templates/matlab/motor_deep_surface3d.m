function fig = motor_deep_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 2318, 'electric motor analysis: 3D response surface', 'electric motor analysis', '3D response surface');
end
