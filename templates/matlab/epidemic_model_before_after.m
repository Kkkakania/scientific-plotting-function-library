function fig = epidemic_model_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3520, 'epidemic dynamics: before-after slope', 'epidemic dynamics', 'before-after slope');
end
