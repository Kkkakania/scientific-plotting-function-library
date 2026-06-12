function fig = hvdc_facts_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3707, 'HVDC and FACTS analysis: multi-metric radar', 'HVDC and FACTS analysis', 'multi-metric radar');
end
