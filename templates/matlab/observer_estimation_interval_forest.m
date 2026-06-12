function fig = observer_estimation_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 1715, 'observer and state estimation: interval forest', 'observer and state estimation', 'interval forest');
end
