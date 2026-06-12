function fig = acoustic_voice_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3110, 'acoustic and voice analysis: polar signature', 'acoustic and voice analysis', 'polar signature');
end
