function fig = protection_fault_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 4012, 'protection and fault analysis: distribution shift', 'protection and fault analysis', 'distribution shift');
end
