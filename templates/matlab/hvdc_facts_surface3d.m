function fig = hvdc_facts_surface3d()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('surface3d', 3718, 'HVDC and FACTS analysis: 3D response surface', 'HVDC and FACTS analysis', '3D response surface');
end
