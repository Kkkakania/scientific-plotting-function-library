function fig = model_diagnostics_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 1502, 'model diagnostics: control limit watch', 'model diagnostics', 'control limit watch');
end
