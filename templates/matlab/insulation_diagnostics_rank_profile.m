function fig = insulation_diagnostics_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3906, 'insulation diagnostics: ranked metric profile', 'insulation diagnostics', 'ranked metric profile');
end
