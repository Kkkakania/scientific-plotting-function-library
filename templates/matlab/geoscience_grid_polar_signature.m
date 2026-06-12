function fig = geoscience_grid_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 4510, 'geoscience grid analysis: polar signature', 'geoscience grid analysis', 'polar signature');
end
