function fig = fluid_cfd_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 2607, 'fluid and CFD analysis: multi-metric radar', 'fluid and CFD analysis', 'multi-metric radar');
end
