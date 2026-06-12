function fig = microgrid_market_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 3810, 'microgrid and market analysis: polar signature', 'microgrid and market analysis', 'polar signature');
end
