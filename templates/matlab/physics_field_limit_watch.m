function fig = physics_field_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 2002, 'physics field analysis: control limit watch', 'physics field analysis', 'control limit watch');
end
