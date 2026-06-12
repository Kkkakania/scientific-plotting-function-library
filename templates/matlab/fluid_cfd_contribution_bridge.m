function fig = fluid_cfd_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2608, 'fluid and CFD analysis: contribution waterfall', 'fluid and CFD analysis', 'contribution waterfall');
end
