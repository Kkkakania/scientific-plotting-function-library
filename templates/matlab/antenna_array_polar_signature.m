function fig = antenna_array_polar_signature()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('polar_profile', 4210, 'antenna array analysis: polar signature', 'antenna array analysis', 'polar signature');
end
