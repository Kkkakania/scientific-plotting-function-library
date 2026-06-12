function fig = fluid_cfd_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 2610, 'fluid and CFD analysis: polar signature', 'fluid and CFD analysis', 'polar signature');
end
