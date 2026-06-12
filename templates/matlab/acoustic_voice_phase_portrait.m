function fig = acoustic_voice_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3111, 'acoustic and voice analysis: phase portrait', 'acoustic and voice analysis', 'phase portrait');
end
