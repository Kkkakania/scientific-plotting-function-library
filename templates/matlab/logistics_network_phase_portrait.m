function fig = logistics_network_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3411, 'logistics and network analysis: phase portrait', 'logistics and network analysis', 'phase portrait');
end
