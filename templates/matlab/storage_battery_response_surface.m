function fig = storage_battery_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2404, 'storage and battery analysis: response contour surface', 'storage and battery analysis', 'response contour surface');
end
