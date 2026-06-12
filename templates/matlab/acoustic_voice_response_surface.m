function fig = acoustic_voice_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3104, 'acoustic and voice analysis: response contour surface', 'acoustic and voice analysis', 'response contour surface');
end
