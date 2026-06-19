function fig = plot_csv_workflow(csvPath,outDir)
%PLOT_CSV_WORKFLOW Render a clean-room CSV measurement example.
%   fig = PLOT_CSV_WORKFLOW(csvPath,outDir) reads a CSV file with the
%   columns time_s, voltage_v, current_a, and temperature_c, then exports a
%   two-panel voltage/current figure to PNG and PDF.

if nargin < 1 || isempty(csvPath)
    csvPath = fullfile(fileparts(mfilename('fullpath')),'sample_measurements.csv');
end
if nargin < 2 || isempty(outDir)
    outDir = fullfile(pwd,'out');
end
if ~exist(outDir,'dir')
    mkdir(outDir);
end

T = readtable(csvPath);

fig = figure('Color','w','Units','centimeters','Position',[2 2 8.9 10.7]);
tiledlayout(fig,2,1,'TileSpacing','compact','Padding','compact');

nexttile;
plot(T.time_s,T.voltage_v,'-o','Color',[0 114 178]/255,'LineWidth',1.2,'MarkerSize',4);
ylabel('Voltage (V)');
legend('Voltage','Location','southeast','Box','off');
grid on;
text(0.02,0.92,'(a)','Units','normalized','FontWeight','bold');
set(gca,'FontName','Arial','FontSize',8,'LineWidth',0.75);

nexttile;
plot(T.time_s,T.current_a,'-s','Color',[230 159 0]/255,'LineWidth',1.2,'MarkerSize',4);
xlabel('Time (s)');
ylabel('Current (A)');
legend('Current','Location','southeast','Box','off');
grid on;
text(0.02,0.92,'(b)','Units','normalized','FontWeight','bold');
set(gca,'FontName','Arial','FontSize',8,'LineWidth',0.75);

pngPath = fullfile(outDir,'csv_workflow_voltage_current.png');
pdfPath = fullfile(outDir,'csv_workflow_voltage_current.pdf');
exportgraphics(fig,pngPath,'Resolution',300);
exportgraphics(fig,pdfPath,'ContentType','vector');
end
