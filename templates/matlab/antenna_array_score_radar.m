function fig = antenna_array_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 4207, 'antenna array analysis: multi-metric radar', 'antenna array analysis', 'multi-metric radar');
end
