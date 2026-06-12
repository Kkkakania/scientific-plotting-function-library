function fig = education_diagram_before_after()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('slope', 3220, 'educational diagramming: before-after slope', 'educational diagramming', 'before-after slope');
end
