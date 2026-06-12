function fig = microgrid_market_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3803, 'microgrid and market analysis: state heatmap', 'microgrid and market analysis', 'state heatmap');
end
