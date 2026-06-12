function fig = chemistry_spectra_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 1911, 'chemistry spectra: phase portrait', 'chemistry spectra', 'phase portrait');
end
