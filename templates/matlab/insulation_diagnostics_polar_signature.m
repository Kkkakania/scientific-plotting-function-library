function fig = insulation_diagnostics_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3910, 'insulation diagnostics: polar signature', 'insulation diagnostics', 'polar signature');
end
