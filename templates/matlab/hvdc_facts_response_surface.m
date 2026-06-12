function fig = hvdc_facts_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3704, 'HVDC and FACTS analysis: response contour surface', 'HVDC and FACTS analysis', 'response contour surface');
end
