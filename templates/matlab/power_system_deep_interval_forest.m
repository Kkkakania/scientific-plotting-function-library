function fig = power_system_deep_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 3615, 'power system analysis: interval forest', 'power system analysis', 'interval forest');
end
