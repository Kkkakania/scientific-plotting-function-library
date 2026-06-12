function fig = hvdc_facts_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 3702, 'HVDC and FACTS analysis: control limit watch', 'HVDC and FACTS analysis', 'control limit watch');
end
