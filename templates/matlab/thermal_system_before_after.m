function fig = thermal_system_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2520, 'thermal system analysis: before-after slope', 'thermal system analysis', 'before-after slope');
end
