function render_all(varargin)
%RENDER_ALL  Render all MATLAB templates to gallery/.
%   render_all                    -> all templates
%   render_all line_basic bar_basic
%   render_all --tag heatmap

    here = fileparts(mfilename('fullpath'));
    addpath(fullfile(here, 'templates', 'matlab'));
    addpath(fullfile(here, '_utils', 'matlab'));

    out = fullfile(here, 'gallery');
    if ~exist(out, 'dir'), mkdir(out); end

    manifest = jsondecode(fileread(fullfile(here, 'manifest.json')));
    names = {manifest.templates.name};

    if nargin >= 1 && strcmp(varargin{1}, '--tag')
        tag = varargin{2};
        keep = false(1, numel(names));
        for k = 1:numel(names)
            keep(k) = any(strcmp(manifest.templates(k).tags, tag));
        end
        names = names(keep);
    elseif nargin >= 1
        names = varargin;
    end

    fprintf('Rendering %d template(s) ...\n', numel(names));
    ok = 0; fail = {};
    for k = 1:numel(names)
        name = names{k};
        try
            fig = feval(name);
            save_figure(fig, name, out, {'png'});
            close(fig);
            ok = ok + 1;
            fprintf('  OK    %s\n', name);
        catch ME
            fail{end+1} = name;
            fprintf('  FAIL  %s : %s\n', name, ME.message);
        end
    end
    fprintf('\nDone: %d ok, %d failed\n', ok, numel(fail));
end
