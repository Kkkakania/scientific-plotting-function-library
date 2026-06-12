function fig = thermal_system_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 2512, 'thermal system analysis: distribution shift', 'thermal system analysis', 'distribution shift');
end
