function fig = materials_microstructure_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 1807, 'materials microstructure: multi-metric radar', 'materials microstructure', 'multi-metric radar');
end
