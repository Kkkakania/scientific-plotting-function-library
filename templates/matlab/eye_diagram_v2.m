function fig = eye_diagram_v2()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(0);
    alpha = 0.35; sps = 16; n_sym = 600; noise = 0.06; isi = 0.25;
    t = (-4*sps : 4*sps) / sps;
    h = rc_pulse(t, alpha);                   % raised-cosine pulse
    sym = 2*(rand(1, n_sym) > 0.5) - 1;
    x = zeros(1, n_sym*sps); x(1:sps:end) = sym;
    y = conv(x, h, 'same');
    y(6:end) = y(6:end) + isi*y(1:end-5);     % residual multipath ISI
    y = y + noise*randn(size(y));
    starts = (20 : n_sym - 23) * sps;         % 0-based sample offsets
    idx = starts' + (1 : 2*sps + 1);          % each row = one 2-UI trace
    segs = y(idx);
    t_ui = ((0 : 2*sps) - sps) / sps;
    n_tr = size(segs, 1);
    X = [repmat(t_ui, n_tr, 1), nan(n_tr, 1)]';
    Y = [segs, nan(n_tr, 1)]';
    c = palette('cat',1); cf = 1 - 0.35*(1 - c);   % faded trace colour
    fig = figure; hold on;
    plot(X(:), Y(:), 'Color', cf, 'LineWidth', 0.7);
    yl = ylim;
    plot([0 0], yl, '--', 'Color', palette('cat',2), 'LineWidth', 1);
    text(0.03, yl(2)*0.92, 'optimum sampling', 'FontSize', 7, 'Color', palette('cat',2));
    ylim(yl);
    xlabel('time (UI)'); ylabel('amplitude');
    title('Eye diagram (raised cosine, \alpha=0.35)');
    grid on;
end

function h = rc_pulse(t, alpha)
    den = 1 - (2*alpha*t).^2;
    sing = abs(den) < 1e-9;
    den(sing) = 1;
    h = sinc_(t) .* cos(pi*alpha*t) ./ den;
    h(sing) = pi/4 * sinc_(1/(2*alpha));
end

function s = sinc_(t)
    s = ones(size(t));
    nz = t ~= 0;
    s(nz) = sin(pi*t(nz)) ./ (pi*t(nz));
end
