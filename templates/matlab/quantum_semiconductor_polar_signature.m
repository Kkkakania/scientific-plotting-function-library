function fig = quantum_semiconductor_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3010, 'quantum and semiconductor analysis: polar signature', 'quantum and semiconductor analysis', 'polar signature');
end
