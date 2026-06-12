function fig = hvdc_facts_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 3711, 'HVDC and FACTS analysis: phase portrait', 'HVDC and FACTS analysis', 'phase portrait');
end
