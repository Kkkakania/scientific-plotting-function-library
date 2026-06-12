function fig = acoustic_voice_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3108, 'acoustic and voice analysis: contribution waterfall', 'acoustic and voice analysis', 'contribution waterfall');
end
