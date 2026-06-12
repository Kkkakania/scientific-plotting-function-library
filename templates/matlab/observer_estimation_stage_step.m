function fig = observer_estimation_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 1717, 'observer and state estimation: stage step curve', 'observer and state estimation', 'stage step curve');
end
