function fig = antenna_array_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 4220, 'antenna array analysis: before-after slope', 'antenna array analysis', 'before-after slope');
end
