function fig = model_diagnostics_interval_forest()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('interval_forest', 1515, 'model diagnostics: interval forest', 'model diagnostics', 'interval forest');
end
