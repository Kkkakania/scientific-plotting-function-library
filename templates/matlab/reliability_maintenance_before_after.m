function fig = reliability_maintenance_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3320, 'reliability and maintenance: before-after slope', 'reliability and maintenance', 'before-after slope');
end
