function fig = physics_field_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2010, 'physics field analysis: polar signature', 'physics field analysis', 'polar signature');
end
