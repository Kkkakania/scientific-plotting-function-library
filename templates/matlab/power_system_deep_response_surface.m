function fig = power_system_deep_response_surface()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('contour', 3604, 'power system analysis: response contour surface', 'power system analysis', 'response contour surface');
end
