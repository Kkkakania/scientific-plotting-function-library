function fig = bio_signal_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 2704, 'biomedical signal analysis: response contour surface', 'biomedical signal analysis', 'response contour surface');
end
