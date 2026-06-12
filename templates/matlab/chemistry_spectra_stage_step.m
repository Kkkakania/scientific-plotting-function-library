function fig = chemistry_spectra_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 1917, 'chemistry spectra: stage step curve', 'chemistry spectra', 'stage step curve');
end
