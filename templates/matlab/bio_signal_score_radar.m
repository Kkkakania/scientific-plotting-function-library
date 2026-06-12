function fig = bio_signal_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2707, 'biomedical signal analysis: multi-metric radar', 'biomedical signal analysis', 'multi-metric radar');
end
