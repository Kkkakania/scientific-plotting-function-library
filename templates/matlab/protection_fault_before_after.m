function fig = protection_fault_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 4020, 'protection and fault analysis: before-after slope', 'protection and fault analysis', 'before-after slope');
end
