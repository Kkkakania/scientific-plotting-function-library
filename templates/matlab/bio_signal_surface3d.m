function fig = bio_signal_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 2718, 'biomedical signal analysis: 3D response surface', 'biomedical signal analysis', '3D response surface');
end
