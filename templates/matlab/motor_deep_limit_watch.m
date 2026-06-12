function fig = motor_deep_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 2302, 'electric motor analysis: control limit watch', 'electric motor analysis', 'control limit watch');
end
