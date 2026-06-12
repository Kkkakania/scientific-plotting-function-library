function fig = paper_multipanel_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 2202, 'paper multipanel layout: control limit watch', 'paper multipanel layout', 'control limit watch');
end
