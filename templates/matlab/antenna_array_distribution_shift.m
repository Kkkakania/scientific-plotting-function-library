function fig = antenna_array_distribution_shift()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('distribution', 4212, 'antenna array analysis: distribution shift', 'antenna array analysis', 'distribution shift');
end
