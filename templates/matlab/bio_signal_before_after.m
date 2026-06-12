function fig = bio_signal_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2720, 'biomedical signal analysis: before-after slope', 'biomedical signal analysis', 'before-after slope');
end
