function fig = protection_fault_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 4017, 'protection and fault analysis: stage step curve', 'protection and fault analysis', 'stage step curve');
end
