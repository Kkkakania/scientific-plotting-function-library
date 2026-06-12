function fig = motor_deep_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2320, 'electric motor analysis: before-after slope', 'electric motor analysis', 'before-after slope');
end
