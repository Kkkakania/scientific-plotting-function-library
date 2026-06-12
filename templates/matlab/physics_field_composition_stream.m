function fig = physics_field_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 2016, 'physics field analysis: composition stream', 'physics field analysis', 'composition stream');
end
