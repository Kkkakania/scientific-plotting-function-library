function fig = quantum_semiconductor_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 3017, 'quantum and semiconductor analysis: stage step curve', 'quantum and semiconductor analysis', 'stage step curve');
end
