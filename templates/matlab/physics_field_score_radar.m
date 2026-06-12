function fig = physics_field_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2007, 'physics field analysis: multi-metric radar', 'physics field analysis', 'multi-metric radar');
end
