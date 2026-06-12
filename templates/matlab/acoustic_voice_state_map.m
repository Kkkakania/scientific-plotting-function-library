function fig = acoustic_voice_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3103, 'acoustic and voice analysis: state heatmap', 'acoustic and voice analysis', 'state heatmap');
end
