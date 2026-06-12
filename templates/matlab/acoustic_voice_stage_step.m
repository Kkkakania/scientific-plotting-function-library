function fig = acoustic_voice_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3117, 'acoustic and voice analysis: stage step curve', 'acoustic and voice analysis', 'stage step curve');
end
