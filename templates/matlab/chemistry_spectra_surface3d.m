function fig = chemistry_spectra_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 1918, 'chemistry spectra: 3D response surface', 'chemistry spectra', '3D response surface');
end
