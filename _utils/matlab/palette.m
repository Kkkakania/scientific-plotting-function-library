function c = palette(kind, n)
    if nargin < 2, n = []; end
    CAT = [ 0.000 0.447 0.698;
            0.835 0.369 0.000;
            0.000 0.620 0.451;
            0.800 0.475 0.655;
            0.941 0.894 0.259;
            0.337 0.706 0.914;
            0.902 0.624 0.000;
            0.600 0.600 0.600 ];
    switch lower(kind)
        case 'cat'
            if isempty(n), c = CAT;
            else
                c = CAT(mod(n-1, size(CAT,1)) + 1, :);
            end
        case 'seq_blue',    c = grad([1 1 1; 0.20 0.45 0.75], def(n, 256));
        case 'seq_orange',  c = grad([1 1 1; 0.85 0.40 0.10], def(n, 256));
        case 'seq_green',   c = grad([1 1 1; 0.18 0.55 0.34], def(n, 256));
        case 'div'
            m = def(n, 256);
            c = [grad([0.13 0.40 0.67; 1 1 1], floor(m/2)); ...
                 grad([1 1 1; 0.80 0.10 0.13], m - floor(m/2))];
        otherwise, error('unknown palette: %s', kind);
    end
end

function g = grad(stops, n)
    t = linspace(0, 1, n)';
    g = (1-t).*stops(1,:) + t.*stops(2,:);
end

function v = def(x, d), if isempty(x), v = d; else, v = x; end, end
