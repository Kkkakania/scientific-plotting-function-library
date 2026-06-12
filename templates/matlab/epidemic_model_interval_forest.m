function fig = epidemic_model_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 3515, 'epidemic dynamics: interval forest', 'epidemic dynamics', 'interval forest');
end
