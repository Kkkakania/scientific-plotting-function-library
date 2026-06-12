function fig = optimization_viz_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2920, 'optimization visualization: before-after slope', 'optimization visualization', 'before-after slope');
end
