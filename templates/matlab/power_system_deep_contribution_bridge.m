function fig = power_system_deep_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3608, 'power system analysis: contribution waterfall', 'power system analysis', 'contribution waterfall');
end
