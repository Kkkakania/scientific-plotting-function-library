function fig = chemistry_spectra_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 1907, 'chemistry spectra: multi-metric radar', 'chemistry spectra', 'multi-metric radar');
end
