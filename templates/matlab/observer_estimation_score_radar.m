function fig = observer_estimation_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 1707, 'observer and state estimation: multi-metric radar', 'observer and state estimation', 'multi-metric radar');
end
