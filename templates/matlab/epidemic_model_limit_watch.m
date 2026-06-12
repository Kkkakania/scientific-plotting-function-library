function fig = epidemic_model_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 3502, 'epidemic dynamics: control limit watch', 'epidemic dynamics', 'control limit watch');
end
