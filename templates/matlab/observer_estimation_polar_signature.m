function fig = observer_estimation_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 1710, 'observer and state estimation: polar signature', 'observer and state estimation', 'polar signature');
end
