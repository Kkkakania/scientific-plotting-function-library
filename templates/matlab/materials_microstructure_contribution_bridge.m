function fig = materials_microstructure_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 1808, 'materials microstructure: contribution waterfall', 'materials microstructure', 'contribution waterfall');
end
