function fig = insulation_diagnostics_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3908, 'insulation diagnostics: contribution waterfall', 'insulation diagnostics', 'contribution waterfall');
end
