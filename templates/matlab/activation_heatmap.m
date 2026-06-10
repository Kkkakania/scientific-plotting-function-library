function fig = activation_heatmap()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(7);
    acts = tanh(randn(32, 50)*1.5);
    fig = figure('Position',[100 100 700 400]);
    imagesc(acts, [-1 1]);
    colormap(palette('div')); cb = colorbar; cb.Label.String = 'activation';
    xlabel('sample'); ylabel('neuron'); title('Hidden layer activations');
end
