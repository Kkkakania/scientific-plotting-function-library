function fig = storage_battery_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2408, 'storage and battery analysis: contribution waterfall', 'storage and battery analysis', 'contribution waterfall');
end
