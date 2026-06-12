function fig = materials_microstructure_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 1806, 'materials microstructure: ranked metric profile', 'materials microstructure', 'ranked metric profile');
end
