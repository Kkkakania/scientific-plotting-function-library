function fig = hvdc_facts_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 3706, 'HVDC and FACTS analysis: ranked metric profile', 'HVDC and FACTS analysis', 'ranked metric profile');
end
