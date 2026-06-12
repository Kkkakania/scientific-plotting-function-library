function fig = optimization_viz_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2910, 'optimization visualization: polar signature', 'optimization visualization', 'polar signature');
end
