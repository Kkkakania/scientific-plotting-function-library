function fig = protection_fault_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 4010, 'protection and fault analysis: polar signature', 'protection and fault analysis', 'polar signature');
end
