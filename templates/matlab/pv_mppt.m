function fig = pv_mppt()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    V = linspace(0, 22, 300);
    Isc = 8.2; Voc = 22;
    I = Isc * (1 - exp((V - Voc)/2)); I(I<0)=0; I(I>Isc)=Isc;
    P = V .* I;
    track_V = [5 8 12 15 17 18 18.5]; track_P = interp1(V, P, track_V);
    [Pmax, idx] = max(P);
    fig = figure;
    plot(V, P, 'Color', palette('cat',1), 'LineWidth', 1.5); hold on;
    plot(track_V, track_P, '-o', 'Color', palette('cat',2), 'MarkerSize', 7);
    scatter(V(idx), Pmax, 120, 'r', 'filled', 'p');
    xlabel('V'); ylabel('P (W)'); title('MPPT P-V tracking');
    legend({'P-V','tracking','MPP'}); grid on;
end
