function fig = model_diagnostics_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 1506, 'model diagnostics: ranked metric profile', 'model diagnostics', 'ranked metric profile');
end
