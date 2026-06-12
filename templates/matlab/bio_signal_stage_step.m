function fig = bio_signal_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2717, 'biomedical signal analysis: stage step curve', 'biomedical signal analysis', 'stage step curve');
end
