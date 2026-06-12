function fig = hvdc_facts_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3703, 'HVDC and FACTS analysis: state heatmap', 'HVDC and FACTS analysis', 'state heatmap');
end
