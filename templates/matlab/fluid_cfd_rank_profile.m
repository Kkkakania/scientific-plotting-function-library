function fig = fluid_cfd_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2606, 'fluid and CFD analysis: ranked metric profile', 'fluid and CFD analysis', 'ranked metric profile');
end
