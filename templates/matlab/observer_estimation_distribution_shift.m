function fig = observer_estimation_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 1712, 'observer and state estimation: distribution shift', 'observer and state estimation', 'distribution shift');
end
