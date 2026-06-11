# 模板目录（274 个）

共 274 个模板，覆盖 26 大类。

每个在 `templates/python/<name>.py` 和 `templates/matlab/<name>.m` 各有一份对照实现。


## 基础 (basic)

| 名称 | 标签 | 说明 |
|---|---|---|
| `line_basic` | line / trend | 单条折线 |
| `line_multi` | line / trend / compare | 多条折线对比 |
| `line_step` | line / step / discrete | 阶梯折线 |
| `line_filled` | line / area | 曲线+下方填充 |
| `line_smoothed` | line / smoothing | 原始+滑动平均 |
| `line_log` | line / log | 半对数/双对数图 |
| `scatter_basic` | scatter | 单组散点 |
| `scatter_grouped` | scatter / category | 按类别着色散点 |
| `scatter_sized` | scatter / bubble | 气泡图 |
| `scatter_colored` | scatter / colormap | 连续色映射散点 |
| `line_with_markers` | line / marker | 带显著标记折线 |
| `line_dashed_styles` | line / style | 不同线型对照 |

## 分类/柱状 (categorical)

| 名称 | 标签 | 说明 |
|---|---|---|
| `bar_basic` | bar | 单系列柱状 |
| `bar_grouped` | bar / group | 分组柱状 |
| `bar_stacked` | bar / stack | 堆叠柱状 |
| `bar_horizontal` | bar / horizontal | 横向条形 |
| `bar_diverging` | bar / diverge / tornado | 发散柱状/龙卷风 |
| `bar_lollipop` | lollipop | 棒棒糖图 |
| `bar_dumbbell` | dumbbell / pair | 哑铃图 |
| `bar_waterfall` | waterfall | 瀑布图 |
| `bar_error` | bar / error | 柱状+误差棒 |
| `bar_percent_stack` | bar / percent | 100% 堆叠柱状 |
| `bar_pareto` | pareto / cumulative | 帕累托图 |
| `bar_combo` | bar / line / combo | 柱+折线组合 |
| `population_pyramid` | pyramid / bidirectional | 人口金字塔 |
| `pie_donut` | pie / donut / proportion | 环形占比图 |
| `bar_progress_bead` | progress / bead | 滑珠进度柱状图 |
| `bar_hatched` | bar / hatch / texture | 带填充纹理柱状图 |
| `bar_overlay_mckinsey` | bar / overlay / business | 麦肯锡叠加柱状图 |

## 分布 (distribution)

| 名称 | 标签 | 说明 |
|---|---|---|
| `histogram_basic` | histogram | 基础直方图 |
| `histogram_overlay` | histogram / compare | 多组叠加直方 |
| `histogram_2d` | hist2d / density | 二维直方图 |
| `histogram_step` | histogram / step | 阶梯直方图 |
| `box_basic` | box | 基础箱线图 |
| `box_jittered` | box / jitter | 箱线+jitter散点 |
| `box_notched` | box / notch | 带凹槽箱线 |
| `violin_basic` | violin | 小提琴图 |
| `violin_split` | violin / split | 左右拆分小提琴 |
| `ridgeline` | ridgeline / density | 山脊图 |
| `violin_with_box` | violin / box | 小提琴+内嵌箱线 |
| `ecdf` | ecdf / cumulative | 经验累积分布 |
| `histogram_cumulative` | histogram / cumulative | 累积直方图 |
| `histogram_log` | histogram / log | 对数分箱直方图 |
| `dist_normal_family` | normal / pdf | 正态分布族 |
| `dist_t_family` | t / pdf | t 分布族 |
| `dist_chi_family` | chi2 / pdf | 卡方分布族 |
| `dist_beta_family` | beta / pdf | Beta 分布族 |
| `dist_mixture` | GMM / mixture | 高斯混合 |
| `swarm_plot` | swarm | 蜂群图 |
| `raincloud` | raincloud | 雨云图 |

## 统计推断 (statistical)

| 名称 | 标签 | 说明 |
|---|---|---|
| `errorbar_basic` | errorbar | 标准误差棒 |
| `errorbar_filled` | band / error | 阴影误差带 |
| `confidence_band` | band / group | 多组均值±std |
| `uncertainty_fan` | fan / quantile | 扇形不确定性 |
| `bland_altman` | agreement | Bland-Altman 一致性 |
| `qq_plot` | qq / normality | Q-Q 正态性 |
| `forest_plot` | forest / meta | 森林图 |
| `paired_slope` | slope / paired | 配对斜率 |
| `residual_plot` | residual / regression | 回归残差图 |
| `roc_curve` | roc / auc / classify | ROC + AUC |
| `calibration_curve` | calibration / classify | 校准曲线 |
| `lift_curve` | lift / gain | 增益/提升曲线 |
| `forest_subgroup` | forest / subgroup | 分组森林图 |

## 关系 (relation)

| 名称 | 标签 | 说明 |
|---|---|---|
| `scatter_density` | scatter / density / kde | KDE 着色密度散点 |
| `scatter_regression` | scatter / fit / ci | 散点+回归+95% CI |
| `scatter_marginal_rug` | scatter / rug | 散点+轴边 rug |
| `scatter_3way` | scatter / encoding | 颜色+大小+形状三编码散点 |

## 矩阵/热力图 (matrix)

| 名称 | 标签 | 说明 |
|---|---|---|
| `heatmap_basic` | heatmap | 基础热力图 |
| `heatmap_annotated` | heatmap / annot | 带数值标注热力 |
| `heatmap_clustered` | heatmap / cluster | 聚类后热力图 |
| `correlation_matrix` | corr / heatmap | 相关系数矩阵 |
| `double_triangle_heatmap` | heatmap / triangle | 双三角热力图 |
| `calendar_heatmap` | calendar / heatmap | 日历热力图 |
| `bubble_matrix` | bubble / matrix | 矩阵气泡图 |
| `confusion_matrix` | confusion / classify | 混淆矩阵 |
| `dendrogram` | dendrogram / cluster | 层次聚类树 |
| `heatmap_dendro` | heatmap / dendro | 热力图+侧边树 |
| `matrix_correlogram` | corr / bubble | 气泡+颜色相关阵 |
| `circular_heatmap` | polar / heatmap | 环形热力图 |
| `heatmap_categorical` | heatmap / categorical | 分类热力图 |
| `cube_heatmap` | cube / 3d / heatmap | 魔方热图 |

## 场/等高线 (field)

| 名称 | 标签 | 说明 |
|---|---|---|
| `contour_filled` | contour / filled | 填充等高线 |
| `contour_lines` | contour / iso | 等值线 |
| `density_kde2d` | kde / contour | 2D KDE 等高线 |
| `density_hexbin` | hexbin / density | 六边形分箱 |
| `quiver` | quiver / vector | 矢量场箭头 |
| `streamplot` | stream / vector | 流线图 |
| `contour_3d` | contour / 3d | 三维等高线 |
| `divergence_overlay` | divergence / stream | 散度场+流线 |
| `potential_field` | potential / equipot | 等势线+梯度 |

## 排名/多维 (ranking)

| 名称 | 标签 | 说明 |
|---|---|---|
| `radar_chart` | radar | 雷达图 |
| `parallel_coordinates` | parallel / multivar | 平行坐标 |
| `waffle_chart` | waffle / proportion | 华夫饼图 |
| `dot_plot_grouped` | dot / group | 分组点图 |

## 时间序列 (time)

| 名称 | 标签 | 说明 |
|---|---|---|
| `timeseries_basic` | time / series | 单序列时间 |
| `timeseries_multi` | time / series / compare | 多序列时间 |
| `area_signed` | area / signed | 正负填充区 |
| `area_stacked` | area / stack | 堆叠面积 |
| `autocorrelation` | acf / lag | 自相关函数 |
| `moving_average` | smoothing / window | 移动平均 |
| `seasonal_subseries` | seasonal | 季节子序列图 |
| `lag_plot` | lag / scatter | 滞后散点 |
| `event_timeline` | event / timeline | 多类别事件时间轴 |
| `candlestick` | ohlc / candle | 蜡烛图 |

## 复合布局 (composite)

| 名称 | 标签 | 说明 |
|---|---|---|
| `zoomed_inset` | inset / zoom | 局部放大插图 |
| `broken_axis` | broken / axis | 折断坐标轴 |
| `dual_yaxis` | dual / axis | 双 Y 轴 |
| `joint_marginal` | joint / marginal | 主散点+边缘直方 |
| `small_multiples` | trellis | 小型多图阵列 |

## 流图 (flow)

| 名称 | 标签 | 说明 |
|---|---|---|
| `sankey_basic` | sankey | 桑基流图 |

## 极坐标 (polar)

| 名称 | 标签 | 说明 |
|---|---|---|
| `polar_basic` | polar / curve | 极坐标曲线 |
| `polar_rose` | rose / direction | 极坐标玫瑰图 |
| `polar_scatter` | polar / scatter | 极坐标散点 |
| `polar_heatmap` | polar / heatmap | 极坐标连续热力 |
| `compass_plot` | compass / vector | 罗盘图 |

## 三维 (3d)

| 名称 | 标签 | 说明 |
|---|---|---|
| `surface_3d` | surface | 三维曲面 |
| `wireframe_3d` | wireframe / proj | 线框+投影等高 |
| `scatter_3d` | scatter | 三维散点 |
| `bar_3d` | bar | 三维柱状 |
| `trisurf_3d` | trisurf / irregular | 三角化曲面 |
| `ribbon_3d` | ribbon | 3D 条带 |
| `contour_filled_3d` | contour / filled | 3D 填充等高线 |
| `quiver_3d` | quiver | 3D 矢量场 |
| `slice_3d` | slice | 体积切片 |
| `isosurface` | isosurface | 等值面 |
| `orbital_3d` | spherical_harmonic | 球谐函数 |
| `tube_3d` | tube / helix | 3D 螺旋管 |
| `line_collection_3d` | stacked / curves | 3D 曲线堆叠 |
| `waterfall_3d` | waterfall / spectra | 3D 瀑布谱 |

## 信号处理 (signal)

| 名称 | 标签 | 说明 |
|---|---|---|
| `fft_spectrum` | fft / spectrum | FFT 单边幅值谱 |
| `welch_psd` | welch / psd | Welch PSD |
| `spectrogram` | stft / tf | 时频图 |
| `step_response` | step / system | 阶跃响应 |
| `impulse_response` | impulse | 二阶冲激响应 |
| `pole_zero` | pole / zero | 极点零点图 |
| `cross_correlation` | xcorr / lag | 互相关函数 |
| `cepstrum` | cepstrum / harmonic | 倒谱 |
| `envelope_detect` | hilbert / envelope | Hilbert 包络 |
| `group_delay` | group_delay | 滤波器群延迟 |
| `fir_design` | FIR / filter | FIR 设计 |
| `iir_design` | IIR / filter | IIR 设计对比 |
| `window_compare` | window / leakage | 窗函数对比 |
| `multitaper_psd` | multitaper / PSD | 多窗 PSD |
| `periodogram` | periodogram | 周期图对比 |
| `hilbert_envelope` | hilbert / IF | 瞬时频率 |
| `coherence_plot` | coherence | 相干函数 |
| `pulse_compression` | chirp / matched_filter | 脉冲压缩匹配滤波 |
| `lms_adaptive` | LMS / adaptive | LMS 自适应滤波 |
| `kalman_tracking` | kalman / estimation | 卡尔曼滤波状态估计 |
| `spectral_estimation_compare` | psd / burg / periodogram | 谱估计方法对比 |
| `lfm_chirp` | chirp / stft / timefreq | LFM 信号时频分析 |

## 电气专题 (electrical)

| 名称 | 标签 | 说明 |
|---|---|---|
| `bode_diagram` | bode / frequency | Bode 幅频+相频 |
| `nyquist_diagram` | nyquist / frequency | Nyquist 频率特性 |
| `smith_chart` | smith / impedance | Smith 圆图 |
| `three_phase_waveform` | three-phase / phasor | 三相波形+相量 |
| `power_triangle` | P / Q / S | 有功-无功-视在三角形 |
| `impedance_locus` | impedance / RLC | RLC 阻抗轨迹 |
| `wavelet_scalogram` | wavelet / tf | 小波时频图 |
| `harmonic_spectrum` | harmonic / FFT | 谐波频谱条形 |
| `thd_bars` | THD / compare | 多负载 THD 对比 |
| `voltage_sag` | sag / event | 电压暂降事件 |
| `inrush_current` | inrush / transient | 励磁涌流衰减 |
| `dq_transform` | dq / park | abc→dq0 旋转坐标 |
| `clarke_transform` | clarke / alphabeta | αβ 静止坐标轨迹 |
| `pwm_modulation` | PWM / modulation | 正弦 PWM 波形 |
| `svpwm_hexagon` | SVPWM / hexagon | 空间矢量六边形 |
| `load_curve_daily` | load / peak | 24h 负荷曲线 |
| `iv_curve` | PV / IV | 光伏 I-V P-V 特性 |
| `pv_mppt` | PV / MPPT | MPPT 追踪过程 |
| `power_factor_locus` | PF / locus | 功率因数日变化 |
| `frequency_drift` | frequency / drift | 电网频率漂移 |
| `dc_ripple` | ripple / filter | 整流纹波滤波 |
| `battery_discharge` | battery / SOC | 电池放电曲线族 |
| `motor_torque_speed` | motor / torque | 电机转矩-转速特性族 |
| `transformer_efficiency` | transformer / efficiency | 变压器效率曲线 |
| `converter_efficiency_map` | converter / efficiency | 变流器效率 MAP |
| `dq_current_locus` | dq / locus / motor | dq 轴电流轨迹 |
| `switching_loss_breakdown` | loss / switching / stacked | 功率器件损耗分解 |
| `thermal_transient` | thermal / junction / foster | 结温暂态曲线 |
| `emi_spectrum` | EMI / CISPR / spectrum | 传导 EMI 频谱 |
| `motor_circle_diagram` | motor / heyland / circle | 感应电机圆图 |

## 控制理论 (control)

| 名称 | 标签 | 说明 |
|---|---|---|
| `root_locus` | root / locus | 根轨迹 |
| `phase_margin` | margin / bode | 增益相位裕度 |
| `sensitivity_function` | S / T | 灵敏度函数族 |
| `ramp_response` | ramp / response | 斜坡响应 |
| `pid_tuning` | PID / step | PID 参数对比 |
| `observer_estimate` | observer / state | 状态观测器估计 |
| `phase_portrait` | phase / portrait | 非线性相图 |
| `limit_cycle` | limit_cycle / vdp | Van der Pol 极限环 |
| `lyapunov_surface` | lyapunov / 3d | Lyapunov 函数曲面 |
| `nichols_chart` | nichols | Nichols 图 |

## RF/通信 (rf)

| 名称 | 标签 | 说明 |
|---|---|---|
| `antenna_pattern_polar` | antenna / polar | 方向图极坐标 |
| `antenna_pattern_3d` | antenna / 3d | 3D 方向图 |
| `vswr_curve` | VSWR / return_loss | VSWR 曲线 |
| `constellation` | QAM / constellation | 星座图 |
| `eye_diagram` | eye / digital | 眼图 |
| `ber_curve` | BER / modulation | 误码率曲线 |
| `capacity_curve` | shannon / capacity | 信道容量 |
| `spectrum_mask` | spectrum / mask | 频谱模板 |

## 机器学习/统计 (ml)

| 名称 | 标签 | 说明 |
|---|---|---|
| `learning_curve` | learning / size | 学习曲线 |
| `precision_recall` | PR / AP | PR 曲线 |
| `silhouette_plot` | silhouette / cluster | 轮廓系数图 |
| `tsne_scatter` | embedding / scatter | 降维散点 |
| `multiclass_roc` | ROC / OvR | 多类 ROC |
| `feature_importance` | importance / bar | 特征重要性 |
| `partial_dependence` | PDP | 偏依赖曲线 |
| `validation_curve` | validation / hyperparam | 超参数验证曲线 |
| `cluster_compare` | cluster / compare | 多算法聚类对比 |
| `shap_summary` | SHAP / explain | SHAP 摘要 |

## 多变量 (multivar)

| 名称 | 标签 | 说明 |
|---|---|---|
| `andrews_curves` | andrews / fourier | Andrews 曲线 |
| `star_plot` | star / radar | 多个雷达星图 |
| `profile_plot` | profile | 剖面图 |
| `pairs_plot` | pairs / scatter | 散点矩阵 |
| `biplot_pca` | PCA / biplot | PCA 双标图 |
| `scree_plot` | PCA / scree | 碎石图 |
| `scatter_matrix` | scatter / matrix / pairs | 散点图矩阵 |

## 特殊可视化 (specialty)

| 名称 | 标签 | 说明 |
|---|---|---|
| `funnel_chart` | funnel / conversion | 漏斗图 |
| `likert_diverging` | likert / survey | Likert 量表 |
| `tree_diagram` | tree / decision | 决策树图 |
| `mosaic_plot` | mosaic / contingency | 马赛克图 |
| `choropleth_grid` | choropleth / grid | 格点 choropleth |
| `treemap_basic` | treemap / hierarchy | 矩形树图 |
| `ternary_scatter` | ternary / composition | 三元相图散点 |

## CFD/流体 (cfd)

| 名称 | 标签 | 说明 |
|---|---|---|
| `velocity_field_cfd` | velocity / quiver | CFD 速度场+矢量箭头 |
| `pressure_contour` | pressure / contour | 压力等高线（圆柱绕流） |
| `vorticity_map` | vorticity | 涡量场 |
| `streamlines_colored` | streamlines | 按速度模值着色流线 |
| `residual_history` | residual / iteration | CFD 迭代残差曲线 |

## 优化算法 (optimization)

| 名称 | 标签 | 说明 |
|---|---|---|
| `convergence_curve` | loss / convergence | 多算法收敛对比 |
| `pareto_front` | pareto / multiobj | Pareto 前沿 |
| `fitness_landscape` | landscape / population | 适应度地形 |
| `ga_evolution` | GA / fitness | GA 适应度演化 |
| `gradient_descent_path` | gradient / path | 梯度下降路径 |

## 神经网络 (nn)

| 名称 | 标签 | 说明 |
|---|---|---|
| `training_curves` | loss / accuracy | 训练曲线（loss+acc） |
| `network_architecture` | architecture | 全连接网络结构图 |
| `decision_boundary` | boundary / classify | 决策边界 |
| `activation_heatmap` | activation | 隐层激活热力图 |
| `weight_distribution` | weight / init | 权重分布对比 |
| `confusion_per_class` | metric / classify | 每类精度/召回/F1 |

## 电力系统 (power)

| 名称 | 标签 | 说明 |
|---|---|---|
| `swing_curve` | stability / transient | 多机功角摇摆曲线 |
| `pv_nose_curve` | voltage / stability | P-V 鼻形曲线 |
| `equal_area_criterion` | stability / criterion | 等面积法则 |
| `relay_tcc` | protection / relay | 反时限保护特性 |
| `fault_oscillography` | fault / oscillography | 三相短路录波 |
| `economic_dispatch` | dispatch / economics | 经济调度等微增率 |
| `feeder_voltage_profile` | distribution / voltage | 馈线电压分布 |
| `grid_frequency_response` | frequency / inertia | 电网频率响应 |
| `generator_capability` | generator / PQ | 发电机运行极限圆图 |
| `line_loading_heatmap` | loading / heatmap | 线路负载率热力图 |
| `phasor_diagram` | phasor / three_phase | 三相电压电流相量图 |
| `pq_injection_heatmap` | injection / heatmap | 节点 PQ 注入热力图 |
| `protection_coordination` | protection / coordination | 阶段式保护配合图 |
| `network_loss_map` | loss / network / flow | 电网网损分布图 |
| `differential_protection` | protection / differential | 差动保护动作特性 |

## 新能源/储能 (energy)

| 名称 | 标签 | 说明 |
|---|---|---|
| `wind_power_curve` | wind / power_curve | 风机功率曲线 |
| `wind_rose` | wind / rose / polar | 风玫瑰图 |
| `solar_irradiance_day` | solar / irradiance | 典型日辐照度 |
| `battery_soc_schedule` | storage / SOC | 储能充放电调度 |
| `duck_curve` | netload / solar | 鸭子曲线 |
| `energy_mix_area` | mix / stacked | 能源结构演化 |
| `ev_charging_load` | EV / load | 电动车充电负荷 |
| `ragone_plot` | storage / ragone | Ragone 储能对比图 |
| `hosting_capacity` | PV / hosting | 光伏承载力箱线 |
| `pv_iv_temperature` | PV / IV / temperature | 光伏 I-V 温度特性 |
| `wake_heatmap` | wind / wake / jensen | 风电场尾流热力图 |
| `pv_mismatch_iv` | PV / mismatch / shading | 光伏失配多峰 I-V |
| `battery_degradation` | battery / aging / DOD | 储能寿命衰减 |

## 流程图/框图 (diagram)

| 名称 | 标签 | 说明 |
|---|---|---|
| `flowchart_algorithm` | flowchart / algorithm | 算法流程图 |
| `flowchart_methodology` | flowchart / methodology | 研究方法流程图 |
| `block_diagram_control` | block / control | 闭环控制框图 |
| `single_line_diagram` | electrical / substation | 电气主接线单线图 |
| `signal_flow_graph` | signal_flow / mason | 信号流图 |
| `graph_directed` | network / directed | 带权重有向图 |
| `graph_undirected` | network / community | 无向图社团 |