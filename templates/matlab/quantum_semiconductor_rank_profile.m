function fig = quantum_semiconductor_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3006, 'quantum and semiconductor analysis: ranked metric profile', 'quantum and semiconductor analysis', 'ranked metric profile');
end
