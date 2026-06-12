function fig = physics_field_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2006, 'physics field analysis: ranked metric profile', 'physics field analysis', 'ranked metric profile');
end
