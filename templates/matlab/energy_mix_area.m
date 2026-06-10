function fig = energy_mix_area()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    apply_theme();
    yr = 2000:2030; x = (yr - 2000)/30;
    coal = 78 - 38*x.^1.3; hydro = 16 + 2*sin(x*3) + x;
    nuclear = 1.5 + 3.5*x; wind = 0.3 + 12*x.^1.8; solar = 0.05 + 14*x.^2.4;
    total = coal + hydro + nuclear + wind + solar;
    shares = [coal; hydro; nuclear; wind; solar]./total*100;
    labels = {'coal', 'hydro', 'nuclear', 'wind', 'solar'};
    fig = figure;
    ar = area(yr, shares');
    for i = 1:5
        ar(i).FaceColor = palette('cat', i); ar(i).FaceAlpha = 0.85;
        ar(i).DisplayName = labels{i};
    end
    xlabel('year'); ylabel('share of generation (%)');
    title('Generation mix evolution'); xlim([2000 2030]); ylim([0 100]);
    legend('Location', 'west', 'FontSize', 8); grid on;
end
