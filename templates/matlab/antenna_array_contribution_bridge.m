function fig = antenna_array_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 4208, 'antenna array analysis: contribution waterfall', 'antenna array analysis', 'contribution waterfall');
end
