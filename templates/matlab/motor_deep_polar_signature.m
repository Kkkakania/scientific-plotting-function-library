function fig = motor_deep_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2310, 'electric motor analysis: polar signature', 'electric motor analysis', 'polar signature');
end
