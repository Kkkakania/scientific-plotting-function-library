function fig = fluid_cfd_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 2615, 'fluid and CFD analysis: interval forest', 'fluid and CFD analysis', 'interval forest');
end
