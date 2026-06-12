function fig = quantum_semiconductor_score_radar()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('radar', 3007, 'quantum and semiconductor analysis: multi-metric radar', 'quantum and semiconductor analysis', 'multi-metric radar');
end
