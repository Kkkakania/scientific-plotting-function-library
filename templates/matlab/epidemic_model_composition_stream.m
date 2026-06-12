function fig = epidemic_model_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 3516, 'epidemic dynamics: composition stream', 'epidemic dynamics', 'composition stream');
end
