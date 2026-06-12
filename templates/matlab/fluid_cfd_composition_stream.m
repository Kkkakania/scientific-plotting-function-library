function fig = fluid_cfd_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 2616, 'fluid and CFD analysis: composition stream', 'fluid and CFD analysis', 'composition stream');
end
