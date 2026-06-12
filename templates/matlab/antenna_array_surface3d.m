function fig = antenna_array_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 4218, 'antenna array analysis: 3D response surface', 'antenna array analysis', '3D response surface');
end
