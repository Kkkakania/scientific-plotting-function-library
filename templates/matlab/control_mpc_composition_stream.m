function fig = control_mpc_composition_stream()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('stacked_area', 1616, 'advanced MPC control: composition stream', 'advanced MPC control', 'composition stream');
end
