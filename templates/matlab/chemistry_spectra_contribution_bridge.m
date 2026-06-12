function fig = chemistry_spectra_contribution_bridge()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('waterfall', 1908, 'chemistry spectra: contribution waterfall', 'chemistry spectra', 'contribution waterfall');
end
