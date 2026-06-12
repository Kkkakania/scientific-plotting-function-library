function fig = acoustic_voice_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3120, 'acoustic and voice analysis: before-after slope', 'acoustic and voice analysis', 'before-after slope');
end
