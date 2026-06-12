function fig = protection_fault_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 4011, 'protection and fault analysis: phase portrait', 'protection and fault analysis', 'phase portrait');
end
