function fig = fluid_cfd_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2613, 'fluid and CFD analysis: interaction bubble matrix', 'fluid and CFD analysis', 'interaction bubble matrix');
end
