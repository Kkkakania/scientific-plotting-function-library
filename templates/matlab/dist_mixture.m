function fig = dist_mixture()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(6);
    n = 1500;
    comps = [0.3 -2 0.7; 0.4 0.5 1.0; 0.3 3 0.6];
    data = [];
    for k = 1:3
        data = [data; comps(k,1)*n*comps(k,3) * randn(round(n*comps(k,1)),1) + comps(k,2)];
    end
    x = linspace(-5, 6, 500);
    pdf = zeros(size(x));
    fig = figure; histogram(data, 60, 'Normalization','pdf', ...
        'FaceColor',[0.8 0.8 0.8], 'EdgeColor','w'); hold on;
    for k = 1:3
        w = comps(k,1); mu = comps(k,2); sd = comps(k,3);
        comp = w/(sd*sqrt(2*pi)) * exp(-(x-mu).^2/(2*sd^2));
        pdf = pdf + comp;
        plot(x, comp, '--', 'Color', palette('cat',k), 'LineWidth', 1);
    end
    plot(x, pdf, 'k', 'LineWidth', 1.5);
    xlabel('x'); ylabel('PDF'); title('Gaussian mixture');
    legend({'data','comp 1','comp 2','comp 3','mixture'}); grid on;
end
