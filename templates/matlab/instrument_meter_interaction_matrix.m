function fig = instrument_meter_interaction_matrix()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('bubble_matrix', 2813, 'instrument and metering: interaction bubble matrix', 'instrument and metering', 'interaction bubble matrix');
end
