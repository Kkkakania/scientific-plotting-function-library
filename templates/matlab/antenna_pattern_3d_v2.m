function fig = antenna_pattern_3d_v2()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    nx = 8; ny = 8; d = 0.5; floor_db = -40;
    theta = linspace(0, pi/2, 121); phi = linspace(0, 2*pi, 241);
    [TH, PH] = meshgrid(theta, phi);
    psix = 2*pi*d*sin(TH).*cos(PH);
    psiy = 2*pi*d*sin(TH).*sin(PH);
    af = af_(nx, psix) .* af_(ny, psiy);
    db = 20*log10(af + 1e-9); db = min(max(db, floor_db), 0);
    r = db - floor_db;
    X = r.*sin(TH).*cos(PH); Y = r.*sin(TH).*sin(PH); Z = r.*cos(TH);
    fig = figure('Position', [100 100 650 520]);
    surf(X, Y, Z, db, 'EdgeColor', 'none');
    colormap(parula); caxis([floor_db 0]);
    cb = colorbar; cb.Label.String = 'normalized gain (dB)';
    xlabel('x'); ylabel('y'); zlabel('z');
    pbaspect([1 1 0.65]);
    title('Planar array 3D pattern (8x8, d=0.5\lambda)');
end

function out = af_(n, psi)
    den = n*sin(psi/2);
    out = abs(sin(n*psi/2) ./ den);
    out(abs(den) < 1e-9) = 1.0;
end
