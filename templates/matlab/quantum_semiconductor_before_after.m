function fig = quantum_semiconductor_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3020, 'quantum and semiconductor analysis: before-after slope', 'quantum and semiconductor analysis', 'before-after slope');
end
