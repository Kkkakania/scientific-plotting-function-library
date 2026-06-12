function fig = physics_field_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2020, 'physics field analysis: before-after slope', 'physics field analysis', 'before-after slope');
end
