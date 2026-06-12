function fig = antenna_array_limit_watch()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('control_limit', 4202, 'antenna array analysis: control limit watch', 'antenna array analysis', 'control limit watch');
end
