function fig = paper_multipanel_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2220, 'paper multipanel layout: before-after slope', 'paper multipanel layout', 'before-after slope');
end
