function fig = bio_signal_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 2708, 'biomedical signal analysis: contribution waterfall', 'biomedical signal analysis', 'contribution waterfall');
end
