function fig = hvdc_facts_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3710, 'HVDC and FACTS analysis: polar signature', 'HVDC and FACTS analysis', 'polar signature');
end
