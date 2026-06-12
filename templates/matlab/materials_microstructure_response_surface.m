function fig = materials_microstructure_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 1804, 'materials microstructure: response contour surface', 'materials microstructure', 'response contour surface');
end
