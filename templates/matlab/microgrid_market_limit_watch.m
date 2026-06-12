function fig = microgrid_market_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 3802, 'microgrid and market analysis: control limit watch', 'microgrid and market analysis', 'control limit watch');
end
