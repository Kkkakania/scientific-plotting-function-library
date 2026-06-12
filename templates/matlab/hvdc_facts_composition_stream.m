function fig = hvdc_facts_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 3716, 'HVDC and FACTS analysis: composition stream', 'HVDC and FACTS analysis', 'composition stream');
end
