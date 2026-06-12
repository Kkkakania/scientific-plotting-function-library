function fig = geoscience_grid_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 4508, 'geoscience grid analysis: contribution waterfall', 'geoscience grid analysis', 'contribution waterfall');
end
