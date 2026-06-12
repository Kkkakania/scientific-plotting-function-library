function fig = materials_microstructure_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 1820, 'materials microstructure: before-after slope', 'materials microstructure', 'before-after slope');
end
