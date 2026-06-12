function fig = model_diagnostics_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 1512, 'model diagnostics: distribution shift', 'model diagnostics', 'distribution shift');
end
