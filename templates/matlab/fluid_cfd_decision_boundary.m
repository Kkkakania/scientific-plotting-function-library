function fig = fluid_cfd_decision_boundary()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('decision_map', 2621, 'fluid and CFD analysis: decision boundary', 'fluid and CFD analysis', 'decision boundary');
end
