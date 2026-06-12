function fig = materials_microstructure_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 1818, 'materials microstructure: 3D response surface', 'materials microstructure', '3D response surface');
end
