function fig = hvdc_facts_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 3712, 'HVDC and FACTS analysis: distribution shift', 'HVDC and FACTS analysis', 'distribution shift');
end
