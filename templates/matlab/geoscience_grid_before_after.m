function fig = geoscience_grid_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 4520, 'geoscience grid analysis: before-after slope', 'geoscience grid analysis', 'before-after slope');
end
