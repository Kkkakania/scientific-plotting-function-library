function fig = observer_estimation_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 1702, 'observer and state estimation: control limit watch', 'observer and state estimation', 'control limit watch');
end
