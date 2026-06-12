function fig = epidemic_model_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3511, 'epidemic dynamics: phase portrait', 'epidemic dynamics', 'phase portrait');
end
