function fig = paper_multipanel_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 2218, 'paper multipanel layout: 3D response surface', 'paper multipanel layout', '3D response surface');
end
