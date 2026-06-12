function fig = paper_multipanel_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2208, 'paper multipanel layout: contribution waterfall', 'paper multipanel layout', 'contribution waterfall');
end
