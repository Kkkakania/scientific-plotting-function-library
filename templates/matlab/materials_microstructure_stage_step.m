function fig = materials_microstructure_stage_step()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('step_curve', 1817, 'materials microstructure: stage step curve', 'materials microstructure', 'stage step curve');
end
