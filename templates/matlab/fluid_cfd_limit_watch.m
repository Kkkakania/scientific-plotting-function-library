function fig = fluid_cfd_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 2602, 'fluid and CFD analysis: control limit watch', 'fluid and CFD analysis', 'control limit watch');
end
