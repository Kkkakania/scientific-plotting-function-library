function fig = power_system_deep_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3610, 'power system analysis: polar signature', 'power system analysis', 'polar signature');
end
