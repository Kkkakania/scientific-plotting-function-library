function fig = model_diagnostics_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 1516, 'model diagnostics: composition stream', 'model diagnostics', 'composition stream');
end
