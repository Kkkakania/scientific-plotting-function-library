function fig = microgrid_market_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3804, 'microgrid and market analysis: response contour surface', 'microgrid and market analysis', 'response contour surface');
end
