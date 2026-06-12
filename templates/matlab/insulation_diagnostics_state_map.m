function fig = insulation_diagnostics_state_map()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('heatmap', 3903, 'insulation diagnostics: state heatmap', 'insulation diagnostics', 'state heatmap');
end
