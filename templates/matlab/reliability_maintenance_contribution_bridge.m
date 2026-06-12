function fig = reliability_maintenance_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3308, 'reliability and maintenance: contribution waterfall', 'reliability and maintenance', 'contribution waterfall');
end
