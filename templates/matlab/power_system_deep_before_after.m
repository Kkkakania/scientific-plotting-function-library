function fig = power_system_deep_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3620, 'power system analysis: before-after slope', 'power system analysis', 'before-after slope');
end
