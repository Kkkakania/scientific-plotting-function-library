function fig = model_diagnostics_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 1518, 'model diagnostics: 3D response surface', 'model diagnostics', '3D response surface');
end
