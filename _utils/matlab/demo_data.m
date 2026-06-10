function out = demo_data(kind, varargin)
%DEMO_DATA Synthetic demo data shared by all MATLAB templates.
    rng(0);
    switch kind
        case 'line'
            n = arg(varargin, 1, 100); k = arg(varargin, 2, 1);
            x = linspace(0, 10, n);
            Y = zeros(k, n);
            for i = 1:k
                Y(i,:) = sin(x + (i-1)*pi/4) + 0.05*randn(1,n);
            end
            out = struct('x', x, 'Y', Y);
        case 'scatter'
            n = arg(varargin, 1, 200); g = arg(varargin, 2, 1);
            X = []; Y = []; G = [];
            for k = 1:g
                X = [X; randn(n,1) + (k-1)*2];
                Y = [Y; randn(n,1) + (k-1)*2];
                G = [G; (k-1)*ones(n,1)];
            end
            out = struct('X', X, 'Y', Y, 'G', G);
        case 'groups'
            nc = arg(varargin, 1, 5); ns = arg(varargin, 2, 2);
            out = struct('labels', {arrayfun(@(i)sprintf('cat%d',i),1:nc,'UniformOutput',false)}, ...
                         'values', 10 + 70*rand(ns, nc));
        case 'matrix'
            r = arg(varargin, 1, 8); c = arg(varargin, 2, 10);
            out = rand(r, c);
        case 'timeseries'
            n = arg(varargin, 1, 365); k = arg(varargin, 2, 1);
            t = (0:n-1);
            Y = zeros(k, n);
            for i = 1:k
                Y(i,:) = 0.001*t + sin(2*pi*t/30 + i) + 0.2*randn(1,n) + (i-1)*0.5;
            end
            out = struct('t', t, 'Y', Y);
        case 'signal'
            fs = arg(varargin, 1, 1000); T = arg(varargin, 2, 1);
            N = fs*T; t = (0:N-1)/fs;
            sig = sin(2*pi*50*t) + 0.6*sin(2*pi*120*t) + 0.3*randn(1,N);
            out = struct('t', t, 'sig', sig, 'fs', fs);
        case 'surface'
            n = arg(varargin, 1, 60);
            [X, Y] = meshgrid(linspace(-3,3,n));
            Z = 3*(1-X).^2 .* exp(-X.^2 - (Y+1).^2) ...
                - 10*(X/5 - X.^3 - Y.^5) .* exp(-X.^2 - Y.^2) ...
                - exp(-(X+1).^2 - Y.^2)/3;
            out = struct('X', X, 'Y', Y, 'Z', Z);
        case 'distribution'
            n = arg(varargin, 1, 500);
            out = randn(n, 1);
        otherwise
            error('Unknown demo data kind: %s', kind);
    end
end

function v = arg(args, idx, d)
    if numel(args) >= idx, v = args{idx}; else, v = d; end
end
