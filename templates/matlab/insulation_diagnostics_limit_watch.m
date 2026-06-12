function fig = insulation_diagnostics_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 3902, 'insulation diagnostics: control limit watch', 'insulation diagnostics', 'control limit watch');
end
