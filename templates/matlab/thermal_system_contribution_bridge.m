function fig = thermal_system_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2508, 'thermal system analysis: contribution waterfall', 'thermal system analysis', 'contribution waterfall');
end
