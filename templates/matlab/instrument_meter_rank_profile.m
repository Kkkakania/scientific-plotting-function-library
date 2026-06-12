function fig = instrument_meter_rank_profile()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('rank_bar', 2806, 'instrument and metering: ranked metric profile', 'instrument and metering', 'ranked metric profile');
end
