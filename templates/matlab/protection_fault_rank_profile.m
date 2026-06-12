function fig = protection_fault_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 4006, 'protection and fault analysis: ranked metric profile', 'protection and fault analysis', 'ranked metric profile');
end
