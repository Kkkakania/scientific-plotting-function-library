function fig = materials_microstructure_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 1811, 'materials microstructure: phase portrait', 'materials microstructure', 'phase portrait');
end
