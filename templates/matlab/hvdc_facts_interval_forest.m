function fig = hvdc_facts_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 3715, 'HVDC and FACTS analysis: interval forest', 'HVDC and FACTS analysis', 'interval forest');
end
