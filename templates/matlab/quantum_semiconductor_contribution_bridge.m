function fig = quantum_semiconductor_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3008, 'quantum and semiconductor analysis: contribution waterfall', 'quantum and semiconductor analysis', 'contribution waterfall');
end
