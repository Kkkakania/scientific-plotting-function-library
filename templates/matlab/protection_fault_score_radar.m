function fig = protection_fault_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 4007, 'protection and fault analysis: multi-metric radar', 'protection and fault analysis', 'multi-metric radar');
end
