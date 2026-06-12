function fig = observer_estimation_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 1720, 'observer and state estimation: before-after slope', 'observer and state estimation', 'before-after slope');
end
