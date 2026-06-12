function out = sci_palettes(name, n)
%SCI_PALETTES  科研配色库（79 套，自动生成勿手改）
%   colors  = sci_palettes('wong')              % 分类色，N×3
%   cmap    = sci_palettes('blues', 256)        % 顺序/发散/周期色，n×3
%   sci_palettes_list()                         % 列出所有名字
%
% 本文件由 scripts/sync_matlab_palettes.py 从 Python 源生成。
    if nargin < 2, n = 256; end

    switch lower(name)
        % ---------- 分类 ----------
        case 'wong'
            out = h2r({'#000000','#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7'});
        case 'okabe_ito'
            out = h2r({'#E69F00','#56B4E9','#009E73','#F0E442','#0072B2','#D55E00','#CC79A7','#999999'});
        case 'duo_warm_cool'
            out = h2r({'#0072B2','#D55E00'});
        case 'duo_blue_red'
            out = h2r({'#1f77b4','#d62728'});
        case 'muted5'
            out = h2r({'#4C72B0','#DD8452','#55A868','#C44E52','#8172B3'});
        case 'bright6'
            out = h2r({'#3a86ff','#fb5607','#ffbe0b','#8338ec','#ff006e','#06d6a0'});
        case 'earth7'
            out = h2r({'#7F4F24','#936639','#A68A64','#BCB382','#C2C5AA','#A4AC86','#656D4A'});
        case 'deep6'
            out = h2r({'#003049','#D62828','#F77F00','#FCBF49','#06A77D','#7251B5'});
        case 'gray5'
            out = h2r({'#1a1a1a','#4d4d4d','#808080','#b3b3b3','#e6e6e6'});
        case 'paper4'
            out = h2r({'#2E5077','#A8A8B3','#E08B6F','#D62246'});
        case 'nature_soft'
            out = h2r({'#3A6A8A','#E8AA42','#A23B72','#5BA689','#C95B4F'});
        case 'science_bold'
            out = h2r({'#1A6FDF','#FF5733','#37AD6B','#FFC300','#9B51E0','#00B7A8'});
        case 'ieee_tech'
            out = h2r({'#003F7F','#5E81AC','#88C0D0','#4C566A','#D08770'});
        case 'bio_dna'
            out = h2r({'#2E8B57','#DC143C','#FF8C00','#1E90FF'});
        case 'high_contrast8'
            out = h2r({'#0D0D0D','#3A4F6B','#6B7280','#8E7CC3','#E8A33D','#D45D5D','#5BAA72','#E6E6E6'});
        case 'pastel6'
            out = h2r({'#A8DADC','#F1A8B7','#FFE5B4','#C7CEEA','#B5EAD7','#F8B195'});
        case 'ggplot_like'
            out = h2r({'#F8766D','#7CAE00','#00BFC4','#C77CFF','#FFC107','#00BA38'});
        case 'dark_bright7'
            out = h2r({'#E6CF65','#00CFDD','#F58A4A','#77D3A6','#8190E6','#FF7B80','#E1D4D7'});
        case 'dark_muted6'
            out = h2r({'#E7D79E','#4293BF','#7FC592','#BA8AC7','#F78F75','#BDC8D1'});
        case 'vivid6'
            out = h2r({'#005AAB','#DE1655','#379F3D','#F28D1F','#00CFE5','#A5439D'});
        case 'safe10'
            out = h2r({'#004C85','#AC2B59','#37804F','#D75E43','#00A1CC','#B98DEC','#D8AA30','#6AD3C0','#FEC6A7','#D0DFEB'});
        case 'mono_blue4'
            out = h2r({'#B5C9D7','#00A4DE','#0077AD','#324550'});
        case 'mono_warm4'
            out = h2r({'#DAC1BB','#E27E65','#B0533D','#56423D'});
        case 'guofeng5'
            out = h2r({'#004B78','#C54744','#AE9B3E','#D6B0D0','#BFDFC6'});
        case 'shuimo4'
            out = h2r({'#2C3136','#626C74','#9DAEB7','#D74C4E'});
        case 'morandi6'
            out = h2r({'#4B6F86','#B08074','#92AD8E','#C5B3C9','#AC926C','#BAD0D3'});
        case 'econ5'
            out = h2r({'#005C76','#C75A5C','#419EA1','#D0AB72','#746484'});
        case 'reviewer6'
            out = h2r({'#9A201C','#EAD15C','#3ECE85','#00B4D7','#0084E9','#A93C93'});
        case 'electric8'
            out = h2r({'#006281','#008FE3','#CDADFF','#A93272','#EC7362','#FFC96A','#527F1D','#00C297'});
        case 'system10'
            out = h2r({'#8D1E79','#FF82A1','#D6663C','#7B5700','#ACCF5C','#00AB66','#00817C','#00EAFF','#00AEFF','#736CD3'});

        % ---------- 顺序 ----------
        case 'blues'
            out = stops_to_cmap([1 1 1; 0.66 0.84 0.9; 0.13 0.44 0.71], n);
        case 'oranges'
            out = stops_to_cmap([1 1 1; 0.99 0.81 0.64; 0.84 0.36 0.05], n);
        case 'greens'
            out = stops_to_cmap([1 1 1; 0.78 0.91 0.75; 0.13 0.55 0.13], n);
        case 'purples'
            out = stops_to_cmap([1 1 1; 0.85 0.78 0.93; 0.4 0.16 0.5], n);
        case 'reds'
            out = stops_to_cmap([1 1 1; 0.98 0.8 0.74; 0.79 0.13 0.13], n);
        case 'gray_to_blue'
            out = stops_to_cmap([0.95 0.95 0.95; 0.5 0.65 0.75; 0.05 0.2 0.45], n);
        case 'warm_lava'
            out = stops_to_cmap([1 0.95 0.7; 0.99 0.59 0.2; ...
                                 0.85 0.15 0.15; 0.4 0 0.4], n);
        case 'inferno_like'
            out = stops_to_cmap([0 0 0; 0.5 0.05 0.3; ...
                                 1 0.4 0.1; 1 0.85 0.4; ...
                                 1 1 0.9], n);
        case 'turbo_like'
            out = stops_to_cmap([0.18 0.07 0.37; 0.05 0.46 0.7; ...
                                 0.2 0.78 0.65; 0.95 0.83 0.27; ...
                                 0.85 0.2 0.1], n);
        case 'glacier'
            out = stops_to_cmap([1 1 1; 0.75 0.9 0.95; ...
                                 0.2 0.55 0.8; 0.05 0.15 0.35; ...
                                 0 0 0], n);
        case 'thermal'
            out = stops_to_cmap([0 0 0; 0.3 0 0.05; ...
                                 0.75 0.15 0.05; 1 0.55 0.1; ...
                                 1 0.95 0.55; 1 1 1], n);
        case 'ocean_depth'
            out = stops_to_cmap([0.85 0.95 0.95; 0.45 0.75 0.85; ...
                                 0.1 0.4 0.65; 0.02 0.1 0.3], n);
        case 'plasma_like'
            out = stops_to_cmap([0.05 0.03 0.53; 0.49 0.01 0.65; ...
                                 0.8 0.27 0.47; 0.97 0.55 0.2; ...
                                 0.99 0.91 0.14], n);
        case 'material_blue'
            out = stops_to_cmap([0.93 0.95 0.98; 0.58 0.77 0.91; ...
                                 0.21 0.51 0.78; 0.05 0.2 0.4], n);
        case 'forest'
            out = stops_to_cmap([0.908 0.972 0.91; 0.607 0.849 0.629; ...
                                 0.34 0.708 0.404; 0.167 0.551 0.261; ...
                                 0.154 0.385 0.198; 0.169 0.219 0.172], n);
        case 'wine'
            out = stops_to_cmap([1 0.93 0.963; 1 0.696 0.818; ...
                                 0.948 0.481 0.671; 0.776 0.324 0.518; ...
                                 0.532 0.243 0.363; 0.261 0.186 0.213], n);
        case 'amber'
            out = stops_to_cmap([1 0.956 0.895; 1 0.776 0.527; ...
                                 0.9 0.614 0.241; 0.74 0.478 0.092; ...
                                 0.543 0.366 0.136; 0.318 0.269 0.22], n);
        case 'teal_deep'
            out = stops_to_cmap([0.865 0.978 0.969; 0.472 0.844 0.824; ...
                                 0 0.694 0.673; 0 0.529 0.513; ...
                                 0 0.357 0.346; 0.094 0.189 0.183], n);
        case 'violet_night'
            out = stops_to_cmap([0.944 0.936 1; 0.755 0.742 1; ...
                                 0.558 0.563 0.921; 0.384 0.404 0.744; ...
                                 0.256 0.265 0.483; 0.146 0.142 0.198], n);
        case 'steel'
            out = stops_to_cmap([0.863 0.959 1; 0.643 0.815 0.891; ...
                                 0.445 0.671 0.764; 0.296 0.526 0.615; ...
                                 0.211 0.383 0.449; 0.16 0.245 0.28], n);
        case 'cool_warm_seq'
            out = stops_to_cmap([0.205 0.29 0.326; 0 0.404 0.675; ...
                                 0.407 0.446 0.87; 0.826 0.46 0.851; ...
                                 1 0.581 0.748; 0.914 0.809 0.803], n);
        case 'dark_lumen'
            out = stops_to_cmap([0.102 0.123 0.176; 0.336 0.193 0.459; ...
                                 0.711 0.201 0.509; 0.945 0.374 0.443; ...
                                 0.994 0.653 0.485; 0.949 0.905 0.836], n);
        case 'ink_wash'
            out = stops_to_cmap([0.896 0.964 1; 0.705 0.786 0.86; ...
                                 0.526 0.615 0.693; 0.364 0.452 0.525; ...
                                 0.22 0.297 0.359; 0.093 0.154 0.2], n);
        case 'cinnabar'
            out = stops_to_cmap([1 0.931 0.921; 1 0.702 0.674; ...
                                 1 0.493 0.474; 0.84 0.345 0.339; ...
                                 0.591 0.272 0.261; 0.303 0.222 0.215], n);
        case 'bamboo'
            out = stops_to_cmap([0.89 0.962 0.905; 0.678 0.839 0.714; ...
                                 0.495 0.709 0.549; 0.364 0.572 0.419; ...
                                 0.285 0.431 0.323; 0.233 0.291 0.246], n);
        case 'storm_current'
            out = stops_to_cmap([0.909 0.958 0.978; 0.553 0.809 0.912; ...
                                 0.198 0.648 0.798; 0 0.476 0.619; ...
                                 0 0.304 0.391; 0.102 0.138 0.153], n);
        case 'copper_heat'
            out = stops_to_cmap([1 0.947 0.917; 0.963 0.722 0.6; ...
                                 0.854 0.516 0.335; 0.673 0.352 0.168; ...
                                 0.441 0.239 0.128; 0.194 0.149 0.127], n);
        case 'aqua_density'
            out = stops_to_cmap([0.893 0.966 0.957; 0.529 0.835 0.805; ...
                                 0.103 0.684 0.648; 0 0.514 0.482; ...
                                 0 0.332 0.311; 0.097 0.154 0.148], n);
        case 'graphite_gold'
            out = stops_to_cmap([0.973 0.952 0.925; 0.89 0.78 0.611; ...
                                 0.763 0.621 0.366; 0.604 0.475 0.228; ...
                                 0.426 0.342 0.193; 0.237 0.222 0.201], n);

        % ---------- 发散 ----------
        case 'blue_white_red'
            out = stops_to_cmap([0.13 0.4 0.67; 1 1 1; 0.8 0.1 0.13], n);
        case 'blue_white_orange'
            out = stops_to_cmap([0.05 0.4 0.7; 1 1 1; 0.95 0.55 0.1], n);
        case 'purple_white_green'
            out = stops_to_cmap([0.45 0.16 0.51; 1 1 1; 0.1 0.55 0.3], n);
        case 'brown_white_teal'
            out = stops_to_cmap([0.55 0.3 0.1; 1 1 1; 0.1 0.55 0.55], n);
        case 'cool_dark_warm'
            out = stops_to_cmap([0.05 0.4 0.7; 0 0 0; 0.85 0.15 0.1], n);
        case 'aurora'
            out = stops_to_cmap([0.45 0.2 0.6; 0.1 0.2 0.5; ...
                                 0.05 0.05 0.1; 0.1 0.45 0.3; ...
                                 0.5 0.85 0.45], n);
        case 'cream_to_teal'
            out = stops_to_cmap([0.85 0.7 0.4; 0.95 0.95 0.92; 0.2 0.55 0.6], n);
        case 'teal_white_rose'
            out = stops_to_cmap([0 0.373 0.37; 0 0.572 0.554; ...
                                 0.533 0.771 0.756; 0.961 0.964 0.963; ...
                                 0.862 0.677 0.756; 0.74 0.393 0.558; ...
                                 0.592 0 0.368], n);
        case 'olive_white_indigo'
            out = stops_to_cmap([0.265 0.296 0; 0.501 0.5 0.225; ...
                                 0.738 0.727 0.586; 0.963 0.963 0.961; ...
                                 0.656 0.723 0.858; 0.314 0.498 0.749; ...
                                 0 0.293 0.635], n);
        case 'earth_div'
            out = stops_to_cmap([0.515 0.248 0.08; 0.686 0.472 0.352; ...
                                 0.838 0.714 0.649; 0.965 0.963 0.962; ...
                                 0.596 0.771 0.774; 0.141 0.581 0.593; ...
                                 0 0.389 0.417], n);
        case 'berry_lime'
            out = stops_to_cmap([0.49 0.155 0.521; 0.654 0.428 0.665; ...
                                 0.814 0.694 0.815; 0.964 0.963 0.964; ...
                                 0.722 0.745 0.599; 0.48 0.538 0.259; ...
                                 0.225 0.339 0], n);
        case 'dark_div'
            out = stops_to_cmap([0 0.862 0.968; 0 0.597 0.662; ...
                                 0.088 0.346 0.374; 0.124 0.126 0.126; ...
                                 0.437 0.268 0.274; 0.781 0.416 0.438; ...
                                 1 0.575 0.619], n);
        case 'guofeng_div'
            out = stops_to_cmap([0 0.324 0.618; 0.274 0.518 0.733; ...
                                 0.645 0.736 0.851; 0.962 0.963 0.965; ...
                                 0.859 0.688 0.668; 0.725 0.423 0.395; ...
                                 0.559 0.134 0.146], n);
        case 'voltage_balance'
            out = stops_to_cmap([0 0.219 0.496; 0.219 0.462 0.654; ...
                                 0.585 0.702 0.805; 0.948 0.948 0.948; ...
                                 0.802 0.644 0.603; 0.636 0.351 0.28; ...
                                 0.447 0 0], n);
        case 'residual_teal_magenta'
            out = stops_to_cmap([0 0.314 0.328; 0.049 0.522 0.523; ...
                                 0.56 0.733 0.73; 0.948 0.948 0.948; ...
                                 0.784 0.65 0.721; 0.609 0.366 0.506; ...
                                 0.42 0.054 0.304], n);
        case 'soil_sky_balance'
            out = stops_to_cmap([0.467 0.234 0; 0.658 0.458 0.257; ...
                                 0.821 0.699 0.593; 0.955 0.955 0.955; ...
                                 0.541 0.754 0.816; 0 0.557 0.681; ...
                                 0 0.366 0.547], n);

        % ---------- 周期 ----------
        case 'twilight_like'
            out = stops_to_cmap([0.25 0.1 0.4; 0.7 0.45 0.7; ...
                                 0.95 0.85 0.6; 0.3 0.65 0.7; ...
                                 0.05 0.2 0.4; 0.25 0.1 0.4], n);
        case 'phase_classic'
            out = stops_to_cmap([1 0.9 0.2; 0.95 0.3 0.2; ...
                                 0.55 0.15 0.5; 0.1 0.3 0.7; ...
                                 1 0.9 0.2], n);
        case 'cyclic_isoL'
            out = stops_to_cmap([0.832 0.447 0.573; 0.81 0.482 0.368; ...
                                 0.655 0.559 0.27; 0.421 0.617 0.355; ...
                                 0 0.641 0.562; 0 0.631 0.768; ...
                                 0.318 0.582 0.856; 0.672 0.501 0.773; ...
                                 0.832 0.447 0.573], n);
        case 'phase_wheel_soft'
            out = stops_to_cmap([0.9 0.45 0.483; 0.815 0.517 0.3; ...
                                 0.631 0.596 0.244; 0.379 0.649 0.365; ...
                                 0 0.671 0.582; 0 0.664 0.798; ...
                                 0 0.622 0.915; 0.596 0.544 0.877; ...
                                 0.835 0.463 0.705; 0.9 0.45 0.483], n);

        otherwise
            error('unknown palette: %s', name);
    end
end

% -------- helpers --------
function rgb = h2r(hex_cells)
    rgb = zeros(numel(hex_cells), 3);
    for i = 1:numel(hex_cells)
        h = hex_cells{i};
        if h(1) == '#', h = h(2:end); end
        rgb(i, :) = [hex2dec(h(1:2)) hex2dec(h(3:4)) hex2dec(h(5:6))] / 255;
    end
end

function cmap = stops_to_cmap(stops, n)
    t = linspace(0, 1, size(stops, 1));
    ti = linspace(0, 1, n);
    cmap = [interp1(t, stops(:,1), ti)' interp1(t, stops(:,2), ti)' interp1(t, stops(:,3), ti)'];
end
