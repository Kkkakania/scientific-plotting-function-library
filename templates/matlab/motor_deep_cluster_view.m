function fig = motor_deep_cluster_view()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('scatter_cluster', 2305, 'electric motor analysis: state cluster scatter', 'electric motor analysis', 'state cluster scatter');
end
