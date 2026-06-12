function fig = hvdc_facts_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3720, 'HVDC and FACTS analysis: before-after slope', 'HVDC and FACTS analysis', 'before-after slope');
end
