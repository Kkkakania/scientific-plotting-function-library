function fig = storage_battery_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 2416, 'storage and battery analysis: composition stream', 'storage and battery analysis', 'composition stream');
end
