function fig = epidemic_model_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3508, 'epidemic dynamics: contribution waterfall', 'epidemic dynamics', 'contribution waterfall');
end
