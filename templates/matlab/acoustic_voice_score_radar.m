function fig = acoustic_voice_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3107, 'acoustic and voice analysis: multi-metric radar', 'acoustic and voice analysis', 'multi-metric radar');
end
