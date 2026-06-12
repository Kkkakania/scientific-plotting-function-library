function fig = bayes_uq_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 4311, 'Bayesian uncertainty quantification: phase portrait', 'Bayesian uncertainty quantification', 'phase portrait');
end
