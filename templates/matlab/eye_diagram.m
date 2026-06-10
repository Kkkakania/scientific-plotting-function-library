function fig = eye_diagram()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme(); rng(1);
    sps = 32; n_sym = 200;
    bits = 2*(rand(n_sym, 1) > 0.5) - 1;
    sig = reshape(repmat(bits.', sps, 1), [], 1);
    k = hann(sps); k = k / sum(k);
    sig = conv(sig, k, 'same') + 0.1*randn(size(sig));
    fig = figure;
    hold on;
    for i = 50:n_sym-1
        seg = sig((i-1)*sps+1 : (i+1)*sps);
        plot(1:numel(seg), seg, 'Color', palette('cat',1), 'LineWidth', 0.6);
    end
    xlabel('sample'); ylabel('amplitude'); title('Eye diagram'); grid on;
end
