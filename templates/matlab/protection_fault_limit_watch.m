function fig = protection_fault_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 4002, 'protection and fault analysis: control limit watch', 'protection and fault analysis', 'control limit watch');
end
