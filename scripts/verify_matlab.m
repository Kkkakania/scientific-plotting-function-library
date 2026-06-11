function verify_matlab(names)
%VERIFY_MATLAB  在本机 MATLAB 里批量实跑全部模板并出报告
%
%   用法（推荐通过 scripts/verify_matlab.sh 调起）：
%       matlab -batch "addpath('scripts'); verify_matlab"
%       matlab -batch "addpath('scripts'); verify_matlab({'bode_diagram'})"
%
%   产出：
%       gallery/matlab/<name>.png        每个模板的 MATLAB 实渲染图
%       docs/matlab_verify_report.md     通过/失败清单（失败含错误信息）

    here = fileparts(mfilename('fullpath'));
    root = fileparts(here);
    cd(root);
    addpath(fullfile(root, 'templates', 'matlab'));
    addpath(fullfile(root, '_utils', 'matlab'));

    % 读 manifest
    raw = fileread(fullfile(root, 'manifest.json'));
    M = jsondecode(raw);
    all_names = arrayfun(@(t) string(t.name), M.templates);
    if nargin >= 1 && ~isempty(names)
        all_names = string(names);
    end

    outdir = fullfile(root, 'gallery', 'matlab');
    if ~exist(outdir, 'dir'), mkdir(outdir); end

    set(0, 'DefaultFigureVisible', 'off');
    n = numel(all_names);
    ok = strings(0); bad = strings(0); msgs = strings(0);
    t0 = tic;
    for i = 1:n
        name = all_names(i);
        try
            fig = feval(char(name));
            if isempty(fig) || ~isgraphics(fig)
                fig = gcf;
            end
            png = fullfile(outdir, char(name + ".png"));
            try
                exportgraphics(fig, png, 'Resolution', 150);
            catch
                saveas(fig, png);   % 老版本回退
            end
            ok(end+1) = name; %#ok<AGROW>
            fprintf('  OK   %3d/%d  %s\n', i, n, name);
        catch ME
            bad(end+1) = name; %#ok<AGROW>
            firstline = strtok(string(ME.message), newline);
            msgs(end+1) = firstline; %#ok<AGROW>
            fprintf('  FAIL %3d/%d  %s  (%s)\n', i, n, name, firstline);
        end
        close all force;
    end
    el = toc(t0);

    % 写报告
    fid = fopen(fullfile(root, 'docs', 'matlab_verify_report.md'), 'w');
    fprintf(fid, '# MATLAB 实跑验证报告\n\n');
    fprintf(fid, '- 日期: %s\n- MATLAB: %s\n- 平台: %s\n', ...
            string(datetime('now')), version, computer);
    fprintf(fid, '- 模板: 通过 **%d** / 失败 **%d**（共 %d，耗时 %.0f s）\n\n', ...
            numel(ok), numel(bad), n, el);
    if ~isempty(bad)
        fprintf(fid, '## 失败清单\n\n| 模板 | 错误 |\n|---|---|\n');
        for k = 1:numel(bad)
            fprintf(fid, '| `%s` | %s |\n', bad(k), msgs(k));
        end
        fprintf(fid, '\n');
    end
    fprintf(fid, '渲染输出: `gallery/matlab/`（%d 张 PNG）\n', numel(ok));
    fclose(fid);
    fprintf('\n完成：%d 过 / %d 失败 → docs/matlab_verify_report.md\n', ...
            numel(ok), numel(bad));
end
