function fig = insulation_diagnostics_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 3916, 'insulation diagnostics: composition stream', 'insulation diagnostics', 'composition stream');
end
