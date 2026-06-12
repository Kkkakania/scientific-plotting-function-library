function fig = antenna_array_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 4211, 'antenna array analysis: phase portrait', 'antenna array analysis', 'phase portrait');
end
