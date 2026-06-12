function fig = protection_fault_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 4016, 'protection and fault analysis: composition stream', 'protection and fault analysis', 'composition stream');
end
