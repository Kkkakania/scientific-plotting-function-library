function fig = epidemic_model_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 3512, 'epidemic dynamics: distribution shift', 'epidemic dynamics', 'distribution shift');
end
