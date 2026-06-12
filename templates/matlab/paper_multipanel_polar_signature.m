function fig = paper_multipanel_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2210, 'paper multipanel layout: polar signature', 'paper multipanel layout', 'polar signature');
end
