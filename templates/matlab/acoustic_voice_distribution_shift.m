function fig = acoustic_voice_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 3112, 'acoustic and voice analysis: distribution shift', 'acoustic and voice analysis', 'distribution shift');
end
