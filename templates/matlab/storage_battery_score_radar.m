function fig = storage_battery_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2407, 'storage and battery analysis: multi-metric radar', 'storage and battery analysis', 'multi-metric radar');
end
