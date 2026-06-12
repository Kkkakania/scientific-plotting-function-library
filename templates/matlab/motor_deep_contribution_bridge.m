function fig = motor_deep_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2308, 'electric motor analysis: contribution waterfall', 'electric motor analysis', 'contribution waterfall');
end
