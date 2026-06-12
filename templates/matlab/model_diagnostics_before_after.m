function fig = model_diagnostics_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 1520, 'model diagnostics: before-after slope', 'model diagnostics', 'before-after slope');
end
