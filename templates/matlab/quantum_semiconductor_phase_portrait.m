function fig = quantum_semiconductor_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3011, 'quantum and semiconductor analysis: phase portrait', 'quantum and semiconductor analysis', 'phase portrait');
end
