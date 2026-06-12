function fig = hvdc_facts_calendar_grid()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('calendar_grid', 3719, 'HVDC and FACTS analysis: calendar grid', 'HVDC and FACTS analysis', 'calendar grid');
end
