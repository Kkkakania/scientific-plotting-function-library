function fig = paper_multipanel_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2207, 'paper multipanel layout: multi-metric radar', 'paper multipanel layout', 'multi-metric radar');
end
