function fig = physics_field_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2008, 'physics field analysis: contribution waterfall', 'physics field analysis', 'contribution waterfall');
end
