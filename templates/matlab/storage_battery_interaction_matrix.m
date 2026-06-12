function fig = storage_battery_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2413, 'storage and battery analysis: interaction bubble matrix', 'storage and battery analysis', 'interaction bubble matrix');
end
