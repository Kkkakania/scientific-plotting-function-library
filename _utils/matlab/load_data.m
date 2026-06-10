function out = load_data(path, kind, varargin)
%LOAD_DATA  统一接口读 CSV / Excel / MAT / TXT 数据
%
%   xy   = load_data('m.csv', 'xy', 'x_col', 'time', 'y_col', 'voltage')
%       -> struct with fields .x, .y
%
%   M    = load_data('hm.xlsx', 'matrix', 'sheet', 'Sheet1')
%       -> 二维数值矩阵
%
%   gp   = load_data('s.csv', 'groups', 'label_col', 'cat', 'value_col', 'count')
%       -> struct with fields .labels (cell), .values (vector)
%
%   ts   = load_data('t.csv', 'timeseries', 'time_col', 1)
%       -> struct with fields .t, .Y (n_series × n_points)
    p = inputParser;
    addParameter(p, 'x_col', 1);
    addParameter(p, 'y_col', 2);
    addParameter(p, 'sheet', '');
    addParameter(p, 'var', '');
    addParameter(p, 'label_col', 1);
    addParameter(p, 'value_col', 2);
    addParameter(p, 'time_col', 1);
    addParameter(p, 'value_cols', []);
    parse(p, varargin{:});
    o = p.Results;

    [~, ~, ext] = fileparts(path); ext = lower(ext);

    switch kind
        case 'xy'
            T = read_any_(path, ext, o.sheet);
            out.x = get_col_(T, o.x_col);
            out.y = get_col_(T, o.y_col);

        case 'matrix'
            switch ext
                case {'.csv', '.tsv', '.txt'}
                    out = readmatrix(path);
                case {'.xls', '.xlsx'}
                    if isempty(o.sheet), out = readmatrix(path);
                    else, out = readmatrix(path, 'Sheet', o.sheet); end
                case '.mat'
                    s = load(path);
                    if isempty(o.var)
                        f = fieldnames(s); var = f{1};
                    else
                        var = o.var;
                    end
                    out = s.(var);
                otherwise
                    error('unsupported: %s', ext);
            end

        case 'groups'
            T = read_any_(path, ext, o.sheet);
            out.labels = get_col_(T, o.label_col);
            out.values = double(get_col_(T, o.value_col));

        case 'timeseries'
            T = read_any_(path, ext, o.sheet);
            out.t = double(get_col_(T, o.time_col));
            if isempty(o.value_cols)
                cols = setdiff(1:width(T), col_idx_(T, o.time_col));
            else
                cols = arrayfun(@(c) col_idx_(T, c), o.value_cols);
            end
            out.Y = double(T{:, cols}).';

        otherwise
            error('unknown kind: %s', kind);
    end
end

function T = read_any_(path, ext, sheet)
    switch ext
        case {'.csv', '.tsv', '.txt'}
            T = readtable(path);
        case {'.xls', '.xlsx'}
            if isempty(sheet), T = readtable(path);
            else, T = readtable(path, 'Sheet', sheet); end
        otherwise
            error('xy/groups/timeseries 不支持: %s', ext);
    end
end

function v = get_col_(T, col)
    if ischar(col) || isstring(col)
        v = T.(char(col));
    else
        v = T{:, col};
    end
end

function i = col_idx_(T, col)
    if ischar(col) || isstring(col)
        i = find(strcmp(T.Properties.VariableNames, char(col)), 1);
    else
        i = col;
    end
end
