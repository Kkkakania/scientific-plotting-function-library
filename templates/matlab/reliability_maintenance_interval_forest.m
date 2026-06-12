function fig = reliability_maintenance_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 3315, 'reliability and maintenance: interval forest', 'reliability and maintenance', 'interval forest');
end
