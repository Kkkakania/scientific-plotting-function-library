function fig = hvdc_facts_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 3705, 'HVDC and FACTS analysis: state cluster scatter', 'HVDC and FACTS analysis', 'state cluster scatter');
end
