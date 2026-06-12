function fig = fluid_cfd_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 2620, 'fluid and CFD analysis: before-after slope', 'fluid and CFD analysis', 'before-after slope');
end
