function fig = materials_microstructure_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 1816, 'materials microstructure: composition stream', 'materials microstructure', 'composition stream');
end
