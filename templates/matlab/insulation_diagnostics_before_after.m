function fig = insulation_diagnostics_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3920, 'insulation diagnostics: before-after slope', 'insulation diagnostics', 'before-after slope');
end
