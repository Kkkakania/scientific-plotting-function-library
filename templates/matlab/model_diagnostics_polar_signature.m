function fig = model_diagnostics_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 1510, 'model diagnostics: polar signature', 'model diagnostics', 'polar signature');
end
