function fig = thermal_system_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2510, 'thermal system analysis: polar signature', 'thermal system analysis', 'polar signature');
end
