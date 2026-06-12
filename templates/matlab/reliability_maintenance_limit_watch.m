function fig = reliability_maintenance_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 3302, 'reliability and maintenance: control limit watch', 'reliability and maintenance', 'control limit watch');
end
