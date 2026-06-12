function fig = microgrid_market_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 3816, 'microgrid and market analysis: composition stream', 'microgrid and market analysis', 'composition stream');
end
