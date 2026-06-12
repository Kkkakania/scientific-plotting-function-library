function fig = insulation_diagnostics_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3911, 'insulation diagnostics: phase portrait', 'insulation diagnostics', 'phase portrait');
end
