function fig = education_diagram_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3206, 'educational diagramming: ranked metric profile', 'educational diagramming', 'ranked metric profile');
end
