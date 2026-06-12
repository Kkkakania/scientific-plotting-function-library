function fig = observer_estimation_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 1704, 'observer and state estimation: response contour surface', 'observer and state estimation', 'response contour surface');
end
