function fig = epidemic_model_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 3518, 'epidemic dynamics: 3D response surface', 'epidemic dynamics', '3D response surface');
end
