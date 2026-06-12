function fig = reliability_maintenance_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3310, 'reliability and maintenance: polar signature', 'reliability and maintenance', 'polar signature');
end
