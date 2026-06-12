function fig = microgrid_market_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3820, 'microgrid and market analysis: before-after slope', 'microgrid and market analysis', 'before-after slope');
end
