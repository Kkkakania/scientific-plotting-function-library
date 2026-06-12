function fig = reliability_maintenance_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3307, 'reliability and maintenance: multi-metric radar', 'reliability and maintenance', 'multi-metric radar');
end
