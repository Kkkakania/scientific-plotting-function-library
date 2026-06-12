function fig = protection_fault_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 4015, 'protection and fault analysis: interval forest', 'protection and fault analysis', 'interval forest');
end
