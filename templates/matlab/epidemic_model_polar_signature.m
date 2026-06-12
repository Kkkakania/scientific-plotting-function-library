function fig = epidemic_model_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3510, 'epidemic dynamics: polar signature', 'epidemic dynamics', 'polar signature');
end
