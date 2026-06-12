function fig = microgrid_market_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 3813, 'microgrid and market analysis: interaction bubble matrix', 'microgrid and market analysis', 'interaction bubble matrix');
end
