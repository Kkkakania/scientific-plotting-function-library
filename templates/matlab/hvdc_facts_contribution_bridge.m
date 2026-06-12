function fig = hvdc_facts_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 3708, 'HVDC and FACTS analysis: contribution waterfall', 'HVDC and FACTS analysis', 'contribution waterfall');
end
