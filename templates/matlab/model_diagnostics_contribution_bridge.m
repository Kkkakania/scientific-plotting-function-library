function fig = model_diagnostics_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 1508, 'model diagnostics: contribution waterfall', 'model diagnostics', 'contribution waterfall');
end
