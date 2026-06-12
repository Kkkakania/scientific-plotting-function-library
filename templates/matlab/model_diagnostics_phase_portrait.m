function fig = model_diagnostics_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 1511, 'model diagnostics: phase portrait', 'model diagnostics', 'phase portrait');
end
