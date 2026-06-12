function fig = materials_microstructure_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 1810, 'materials microstructure: polar signature', 'materials microstructure', 'polar signature');
end
