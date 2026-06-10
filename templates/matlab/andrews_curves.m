function fig = andrews_curves()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    centers = [0 0 0 0 0; 2 1 -1 0.5 0; -1 2 1 -0.5 0.5];
    X = []; labels = [];
    for k = 1:3
        X = [X; randn(20,5)*0.5 + centers(k,:)];
        labels = [labels; k*ones(20,1)];
    end
    t = linspace(-pi, pi, 200);
    fig = figure('Position',[100 100 800 450]); hold on;
    for k = 1:3
        for row = find(labels == k)'
            x = X(row, :);
            y = x(1)/sqrt(2) + x(2)*sin(t) + x(3)*cos(t) + x(4)*sin(2*t) + x(5)*cos(2*t);
            plot(t, y, 'Color', palette('cat',k), 'LineWidth', 0.6);
        end
    end
    xlabel('t'); ylabel('f(t)'); title('Andrews curves'); grid on;
end
