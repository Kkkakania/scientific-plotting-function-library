function fig = observer_estimation_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 1708, 'observer and state estimation: contribution waterfall', 'observer and state estimation', 'contribution waterfall');
end
