function fig = fluid_cfd_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 2617, 'fluid and CFD analysis: stage step curve', 'fluid and CFD analysis', 'stage step curve');
end
