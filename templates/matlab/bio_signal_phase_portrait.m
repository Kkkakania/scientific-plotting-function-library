function fig = bio_signal_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 2711, 'biomedical signal analysis: phase portrait', 'biomedical signal analysis', 'phase portrait');
end
