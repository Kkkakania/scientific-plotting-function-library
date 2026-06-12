function fig = hvdc_facts_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3717, 'HVDC and FACTS analysis: stage step curve', 'HVDC and FACTS analysis', 'stage step curve');
end
