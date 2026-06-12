function fig = matrix_tensor_phase_portrait()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('phase_plane', 4411, 'matrix and tensor visualization: phase portrait', 'matrix and tensor visualization', 'phase portrait');
end
