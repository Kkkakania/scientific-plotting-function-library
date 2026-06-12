function fig = radar_advanced_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 4110, 'advanced radar analysis: polar signature', 'advanced radar analysis', 'polar signature');
end
