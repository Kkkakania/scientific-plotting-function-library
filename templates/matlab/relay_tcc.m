function fig = relay_tcc()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    M = linspace(1.1, 30, 400);
    names = {'standard inverse', 'very inverse', 'extremely inverse'};
    k = [0.14 13.5 80]; a = [0.02 1 2]; tds = [0.3 0.4 0.5];
    fig = figure;
    for i = 1:3
        loglog(M, tds(i)*k(i)./(M.^a(i) - 1), 'Color', palette('cat', i), ...
               'DisplayName', names{i});
        hold on;
    end
    xlabel('current multiple M = I/I_{pickup}'); ylabel('operating time (s)');
    title('Inverse-time overcurrent coordination');
    legend; grid on;
end
