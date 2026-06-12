function fig = chemistry_spectra_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 1902, 'chemistry spectra: control limit watch', 'chemistry spectra', 'control limit watch');
end
