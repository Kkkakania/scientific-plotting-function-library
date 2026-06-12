function fig = materials_microstructure_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 1813, 'materials microstructure: interaction bubble matrix', 'materials microstructure', 'interaction bubble matrix');
end
