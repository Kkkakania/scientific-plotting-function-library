# 模板目录（1000 个）

共 1000 个模板，覆盖 26 大类。

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
| `bayesian_posterior_update` | bayesian / posterior / prior | 贝叶斯后验更新图（先验/似然/后验三曲线） |
| `bland_altman_v2` | agreement / bias / method-comparison | Bland-Altman 一致性图（偏倚+一致性限+密度着色） |
| `bootstrap_ci` | bootstrap / confidence-interval / resampling | Bootstrap 置信区间图（重采样分布+百分位区间） |
| `calibration_curve_v2` | calibration / reliability / probability | 概率校准曲线（分箱可靠性+完美校准参考线） |
| `credible_forest` | bayesian / credible-interval / forest | 可信区间森林图（后验中位数+95%区间） |
| `effect_size_panel` | effect-size / cohen-d / overlap | 两正态分布重叠区+Cohen's d 标尺的效应量面板 |
| `hazard_function` | hazard / weibull / survival | Weibull 风险函数对比（递减/恒定/递增形状参数） |
| `mcmc_trace_panel` | mcmc / trace / posterior | MCMC 迹图面板（4 链 trace+后验密度两列布局） |
| `meta_funnel` | meta-analysis / funnel / publication-bias | Meta 分析漏斗图（效应量 vs 标准误+伪置信漏斗） |
| `permutation_null` | permutation / p-value / resampling | 置换检验零分布（null 直方图+观测统计量+双侧 p 值） |
| `power_curve_analysis` | power / ttest / contour | 双样本t检验统计功效等高线 |
| `pp_plot` | pp / normality / cdf | P-P 概率图对比经验与理论累积概率 |
| `qq_compare_grid` | qq / normality / grid | 多分布 QQ 四宫格对比正态理论分位 |
| `roc_multi_compare` | roc / auc / compare | 多模型 ROC 曲线与 AUC 图例对比 |
| `survival_km` | survival / kaplan-meier / censor | Kaplan-Meier 生存曲线含删失标记与风险人数表 |
| `volatility_cone` | volatility / quantile / finance | 多窗口滚动波动率分位锥加当前值 |
| `reliability_maintenance_monitoring` | reliability / monitoring / time-band | 可靠性与维修监测带状时序（time-band 模式，合成数据） |
| `reliability_maintenance_limit_watch` | reliability / limit_watch / control-limit | 可靠性与维修控制限监测（control-limit 模式，合成数据） |
| `reliability_maintenance_state_map` | reliability / state_map / heatmap | 可靠性与维修状态热力图（heatmap 模式，合成数据） |
| `reliability_maintenance_response_surface` | reliability / response_surface / contour | 可靠性与维修响应等值面（contour 模式，合成数据） |
| `reliability_maintenance_cluster_view` | reliability / cluster_view / cluster | 可靠性与维修状态聚类散点（cluster 模式，合成数据） |
| `reliability_maintenance_rank_profile` | reliability / rank_profile / ranking | 可靠性与维修指标排序条形（ranking 模式，合成数据） |
| `reliability_maintenance_score_radar` | reliability / score_radar / radar | 可靠性与维修多维评分雷达（radar 模式，合成数据） |
| `reliability_maintenance_contribution_bridge` | reliability / contribution_bridge / waterfall | 可靠性与维修贡献瀑布桥（waterfall 模式，合成数据） |
| `reliability_maintenance_scenario_facets` | reliability / scenario_facets / small-multiples | 可靠性与维修场景分面（small-multiples 模式，合成数据） |
| `reliability_maintenance_polar_signature` | reliability / polar_signature / polar | 可靠性与维修极坐标指纹（polar 模式，合成数据） |
| `reliability_maintenance_phase_portrait` | reliability / phase_portrait / phase-plane | 可靠性与维修相平面画像（phase-plane 模式，合成数据） |
| `reliability_maintenance_distribution_shift` | reliability / distribution_shift / distribution | 可靠性与维修分布漂移（distribution 模式，合成数据） |
| `reliability_maintenance_interaction_matrix` | reliability / interaction_matrix / matrix | 可靠性与维修交互气泡矩阵（matrix 模式，合成数据） |
| `reliability_maintenance_factor_lollipop` | reliability / factor_lollipop / lollipop | 可靠性与维修因子棒棒糖（lollipop 模式，合成数据） |
| `reliability_maintenance_interval_forest` | reliability / interval_forest / interval | 可靠性与维修区间森林图（interval 模式，合成数据） |
| `reliability_maintenance_composition_stream` | reliability / composition_stream / stacked-area | 可靠性与维修组成流面积（stacked-area 模式，合成数据） |
| `reliability_maintenance_stage_step` | reliability / stage_step / step | 可靠性与维修阶段阶梯曲线（step 模式，合成数据） |
| `reliability_maintenance_surface3d` | reliability / surface3d / 3d-surface | 可靠性与维修三维响应曲面（3d-surface 模式，合成数据） |
| `reliability_maintenance_calendar_grid` | reliability / calendar_grid / calendar-grid | 可靠性与维修日历网格（calendar-grid 模式，合成数据） |
| `reliability_maintenance_before_after` | reliability / before_after / slope | 可靠性与维修前后斜率对比（slope 模式，合成数据） |
| `reliability_maintenance_decision_boundary` | reliability / decision_boundary / decision-map | 可靠性与维修决策边界图（decision-map 模式，合成数据） |
| `epidemic_model_monitoring` | epidemic / monitoring / time-band | 传播动力学监测带状时序（time-band 模式，合成数据） |
| `epidemic_model_limit_watch` | epidemic / limit_watch / control-limit | 传播动力学控制限监测（control-limit 模式，合成数据） |
| `epidemic_model_state_map` | epidemic / state_map / heatmap | 传播动力学状态热力图（heatmap 模式，合成数据） |
| `epidemic_model_response_surface` | epidemic / response_surface / contour | 传播动力学响应等值面（contour 模式，合成数据） |
| `epidemic_model_cluster_view` | epidemic / cluster_view / cluster | 传播动力学状态聚类散点（cluster 模式，合成数据） |
| `epidemic_model_rank_profile` | epidemic / rank_profile / ranking | 传播动力学指标排序条形（ranking 模式，合成数据） |
| `epidemic_model_score_radar` | epidemic / score_radar / radar | 传播动力学多维评分雷达（radar 模式，合成数据） |
| `epidemic_model_contribution_bridge` | epidemic / contribution_bridge / waterfall | 传播动力学贡献瀑布桥（waterfall 模式，合成数据） |
| `epidemic_model_scenario_facets` | epidemic / scenario_facets / small-multiples | 传播动力学场景分面（small-multiples 模式，合成数据） |
| `epidemic_model_polar_signature` | epidemic / polar_signature / polar | 传播动力学极坐标指纹（polar 模式，合成数据） |
| `epidemic_model_phase_portrait` | epidemic / phase_portrait / phase-plane | 传播动力学相平面画像（phase-plane 模式，合成数据） |
| `epidemic_model_distribution_shift` | epidemic / distribution_shift / distribution | 传播动力学分布漂移（distribution 模式，合成数据） |
| `epidemic_model_interaction_matrix` | epidemic / interaction_matrix / matrix | 传播动力学交互气泡矩阵（matrix 模式，合成数据） |
| `epidemic_model_factor_lollipop` | epidemic / factor_lollipop / lollipop | 传播动力学因子棒棒糖（lollipop 模式，合成数据） |
| `epidemic_model_interval_forest` | epidemic / interval_forest / interval | 传播动力学区间森林图（interval 模式，合成数据） |
| `epidemic_model_composition_stream` | epidemic / composition_stream / stacked-area | 传播动力学组成流面积（stacked-area 模式，合成数据） |
| `epidemic_model_stage_step` | epidemic / stage_step / step | 传播动力学阶段阶梯曲线（step 模式，合成数据） |
| `epidemic_model_surface3d` | epidemic / surface3d / 3d-surface | 传播动力学三维响应曲面（3d-surface 模式，合成数据） |
| `epidemic_model_calendar_grid` | epidemic / calendar_grid / calendar-grid | 传播动力学日历网格（calendar-grid 模式，合成数据） |
| `epidemic_model_before_after` | epidemic / before_after / slope | 传播动力学前后斜率对比（slope 模式，合成数据） |
| `epidemic_model_decision_boundary` | epidemic / decision_boundary / decision-map | 传播动力学决策边界图（decision-map 模式，合成数据） |
| `bayes_uq_monitoring` | bayesian / monitoring / time-band | 贝叶斯与不确定性量化监测带状时序（time-band 模式，合成数据） |
| `bayes_uq_limit_watch` | bayesian / limit_watch / control-limit | 贝叶斯与不确定性量化控制限监测（control-limit 模式，合成数据） |
| `bayes_uq_state_map` | bayesian / state_map / heatmap | 贝叶斯与不确定性量化状态热力图（heatmap 模式，合成数据） |
| `bayes_uq_response_surface` | bayesian / response_surface / contour | 贝叶斯与不确定性量化响应等值面（contour 模式，合成数据） |
| `bayes_uq_cluster_view` | bayesian / cluster_view / cluster | 贝叶斯与不确定性量化状态聚类散点（cluster 模式，合成数据） |
| `bayes_uq_rank_profile` | bayesian / rank_profile / ranking | 贝叶斯与不确定性量化指标排序条形（ranking 模式，合成数据） |
| `bayes_uq_score_radar` | bayesian / score_radar / radar | 贝叶斯与不确定性量化多维评分雷达（radar 模式，合成数据） |
| `bayes_uq_contribution_bridge` | bayesian / contribution_bridge / waterfall | 贝叶斯与不确定性量化贡献瀑布桥（waterfall 模式，合成数据） |
| `bayes_uq_scenario_facets` | bayesian / scenario_facets / small-multiples | 贝叶斯与不确定性量化场景分面（small-multiples 模式，合成数据） |
| `bayes_uq_polar_signature` | bayesian / polar_signature / polar | 贝叶斯与不确定性量化极坐标指纹（polar 模式，合成数据） |
| `bayes_uq_phase_portrait` | bayesian / phase_portrait / phase-plane | 贝叶斯与不确定性量化相平面画像（phase-plane 模式，合成数据） |
| `bayes_uq_distribution_shift` | bayesian / distribution_shift / distribution | 贝叶斯与不确定性量化分布漂移（distribution 模式，合成数据） |
| `bayes_uq_interaction_matrix` | bayesian / interaction_matrix / matrix | 贝叶斯与不确定性量化交互气泡矩阵（matrix 模式，合成数据） |
| `bayes_uq_factor_lollipop` | bayesian / factor_lollipop / lollipop | 贝叶斯与不确定性量化因子棒棒糖（lollipop 模式，合成数据） |
| `bayes_uq_interval_forest` | bayesian / interval_forest / interval | 贝叶斯与不确定性量化区间森林图（interval 模式，合成数据） |
| `bayes_uq_composition_stream` | bayesian / composition_stream / stacked-area | 贝叶斯与不确定性量化组成流面积（stacked-area 模式，合成数据） |
| `bayes_uq_stage_step` | bayesian / stage_step / step | 贝叶斯与不确定性量化阶段阶梯曲线（step 模式，合成数据） |
| `bayes_uq_surface3d` | bayesian / surface3d / 3d-surface | 贝叶斯与不确定性量化三维响应曲面（3d-surface 模式，合成数据） |
| `bayes_uq_calendar_grid` | bayesian / calendar_grid / calendar-grid | 贝叶斯与不确定性量化日历网格（calendar-grid 模式，合成数据） |
| `bayes_uq_before_after` | bayesian / before_after / slope | 贝叶斯与不确定性量化前后斜率对比（slope 模式，合成数据） |
| `bayes_uq_decision_boundary` | bayesian / decision_boundary / decision-map | 贝叶斯与不确定性量化决策边界图（decision-map 模式，合成数据） |

## 关系 (relation)

| 名称 | 标签 | 说明 |
|---|---|---|
| `scatter_density` | scatter / density / kde | KDE 着色密度散点 |
| `scatter_regression` | scatter / fit / ci | 散点+回归+95% CI |
| `scatter_marginal_rug` | scatter / rug | 散点+轴边 rug |
| `scatter_3way` | scatter / encoding | 颜色+大小+形状三编码散点 |
| `arc_diagram` | arc / network / ordered | 弧线网络图（节点按序排列+上弧连边） |
| `hive_plot` | hive / network / bezier | 蜂巢图（3 轴按节点类别放置+轴间贝塞尔连线） |
| `logistics_network_monitoring` | logistics / monitoring / time-band | 物流与网络监测带状时序（time-band 模式，合成数据） |
| `logistics_network_limit_watch` | logistics / limit_watch / control-limit | 物流与网络控制限监测（control-limit 模式，合成数据） |
| `logistics_network_state_map` | logistics / state_map / heatmap | 物流与网络状态热力图（heatmap 模式，合成数据） |
| `logistics_network_response_surface` | logistics / response_surface / contour | 物流与网络响应等值面（contour 模式，合成数据） |
| `logistics_network_cluster_view` | logistics / cluster_view / cluster | 物流与网络状态聚类散点（cluster 模式，合成数据） |
| `logistics_network_rank_profile` | logistics / rank_profile / ranking | 物流与网络指标排序条形（ranking 模式，合成数据） |
| `logistics_network_score_radar` | logistics / score_radar / radar | 物流与网络多维评分雷达（radar 模式，合成数据） |
| `logistics_network_contribution_bridge` | logistics / contribution_bridge / waterfall | 物流与网络贡献瀑布桥（waterfall 模式，合成数据） |
| `logistics_network_scenario_facets` | logistics / scenario_facets / small-multiples | 物流与网络场景分面（small-multiples 模式，合成数据） |
| `logistics_network_polar_signature` | logistics / polar_signature / polar | 物流与网络极坐标指纹（polar 模式，合成数据） |
| `logistics_network_phase_portrait` | logistics / phase_portrait / phase-plane | 物流与网络相平面画像（phase-plane 模式，合成数据） |
| `logistics_network_distribution_shift` | logistics / distribution_shift / distribution | 物流与网络分布漂移（distribution 模式，合成数据） |
| `logistics_network_interaction_matrix` | logistics / interaction_matrix / matrix | 物流与网络交互气泡矩阵（matrix 模式，合成数据） |
| `logistics_network_factor_lollipop` | logistics / factor_lollipop / lollipop | 物流与网络因子棒棒糖（lollipop 模式，合成数据） |
| `logistics_network_interval_forest` | logistics / interval_forest / interval | 物流与网络区间森林图（interval 模式，合成数据） |
| `logistics_network_composition_stream` | logistics / composition_stream / stacked-area | 物流与网络组成流面积（stacked-area 模式，合成数据） |
| `logistics_network_stage_step` | logistics / stage_step / step | 物流与网络阶段阶梯曲线（step 模式，合成数据） |
| `logistics_network_surface3d` | logistics / surface3d / 3d-surface | 物流与网络三维响应曲面（3d-surface 模式，合成数据） |
| `logistics_network_calendar_grid` | logistics / calendar_grid / calendar-grid | 物流与网络日历网格（calendar-grid 模式，合成数据） |
| `logistics_network_before_after` | logistics / before_after / slope | 物流与网络前后斜率对比（slope 模式，合成数据） |
| `logistics_network_decision_boundary` | logistics / decision_boundary / decision-map | 物流与网络决策边界图（decision-map 模式，合成数据） |

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
| `matrix_tensor_monitoring` | tensor / monitoring / time-band | 矩阵与张量可视化监测带状时序（time-band 模式，合成数据） |
| `matrix_tensor_limit_watch` | tensor / limit_watch / control-limit | 矩阵与张量可视化控制限监测（control-limit 模式，合成数据） |
| `matrix_tensor_state_map` | tensor / state_map / heatmap | 矩阵与张量可视化状态热力图（heatmap 模式，合成数据） |
| `matrix_tensor_response_surface` | tensor / response_surface / contour | 矩阵与张量可视化响应等值面（contour 模式，合成数据） |
| `matrix_tensor_cluster_view` | tensor / cluster_view / cluster | 矩阵与张量可视化状态聚类散点（cluster 模式，合成数据） |
| `matrix_tensor_rank_profile` | tensor / rank_profile / ranking | 矩阵与张量可视化指标排序条形（ranking 模式，合成数据） |
| `matrix_tensor_score_radar` | tensor / score_radar / radar | 矩阵与张量可视化多维评分雷达（radar 模式，合成数据） |
| `matrix_tensor_contribution_bridge` | tensor / contribution_bridge / waterfall | 矩阵与张量可视化贡献瀑布桥（waterfall 模式，合成数据） |
| `matrix_tensor_scenario_facets` | tensor / scenario_facets / small-multiples | 矩阵与张量可视化场景分面（small-multiples 模式，合成数据） |
| `matrix_tensor_polar_signature` | tensor / polar_signature / polar | 矩阵与张量可视化极坐标指纹（polar 模式，合成数据） |
| `matrix_tensor_phase_portrait` | tensor / phase_portrait / phase-plane | 矩阵与张量可视化相平面画像（phase-plane 模式，合成数据） |
| `matrix_tensor_distribution_shift` | tensor / distribution_shift / distribution | 矩阵与张量可视化分布漂移（distribution 模式，合成数据） |
| `matrix_tensor_interaction_matrix` | tensor / interaction_matrix / matrix | 矩阵与张量可视化交互气泡矩阵（matrix 模式，合成数据） |
| `matrix_tensor_factor_lollipop` | tensor / factor_lollipop / lollipop | 矩阵与张量可视化因子棒棒糖（lollipop 模式，合成数据） |
| `matrix_tensor_interval_forest` | tensor / interval_forest / interval | 矩阵与张量可视化区间森林图（interval 模式，合成数据） |
| `matrix_tensor_composition_stream` | tensor / composition_stream / stacked-area | 矩阵与张量可视化组成流面积（stacked-area 模式，合成数据） |
| `matrix_tensor_stage_step` | tensor / stage_step / step | 矩阵与张量可视化阶段阶梯曲线（step 模式，合成数据） |
| `matrix_tensor_surface3d` | tensor / surface3d / 3d-surface | 矩阵与张量可视化三维响应曲面（3d-surface 模式，合成数据） |
| `matrix_tensor_calendar_grid` | tensor / calendar_grid / calendar-grid | 矩阵与张量可视化日历网格（calendar-grid 模式，合成数据） |
| `matrix_tensor_before_after` | tensor / before_after / slope | 矩阵与张量可视化前后斜率对比（slope 模式，合成数据） |
| `matrix_tensor_decision_boundary` | tensor / decision_boundary / decision-map | 矩阵与张量可视化决策边界图（decision-map 模式，合成数据） |

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
| `physics_field_monitoring` | physics / monitoring / time-band | 物理场分析监测带状时序（time-band 模式，合成数据） |
| `physics_field_limit_watch` | physics / limit_watch / control-limit | 物理场分析控制限监测（control-limit 模式，合成数据） |
| `physics_field_state_map` | physics / state_map / heatmap | 物理场分析状态热力图（heatmap 模式，合成数据） |
| `physics_field_response_surface` | physics / response_surface / contour | 物理场分析响应等值面（contour 模式，合成数据） |
| `physics_field_cluster_view` | physics / cluster_view / cluster | 物理场分析状态聚类散点（cluster 模式，合成数据） |
| `physics_field_rank_profile` | physics / rank_profile / ranking | 物理场分析指标排序条形（ranking 模式，合成数据） |
| `physics_field_score_radar` | physics / score_radar / radar | 物理场分析多维评分雷达（radar 模式，合成数据） |
| `physics_field_contribution_bridge` | physics / contribution_bridge / waterfall | 物理场分析贡献瀑布桥（waterfall 模式，合成数据） |
| `physics_field_scenario_facets` | physics / scenario_facets / small-multiples | 物理场分析场景分面（small-multiples 模式，合成数据） |
| `physics_field_polar_signature` | physics / polar_signature / polar | 物理场分析极坐标指纹（polar 模式，合成数据） |
| `physics_field_phase_portrait` | physics / phase_portrait / phase-plane | 物理场分析相平面画像（phase-plane 模式，合成数据） |
| `physics_field_distribution_shift` | physics / distribution_shift / distribution | 物理场分析分布漂移（distribution 模式，合成数据） |
| `physics_field_interaction_matrix` | physics / interaction_matrix / matrix | 物理场分析交互气泡矩阵（matrix 模式，合成数据） |
| `physics_field_factor_lollipop` | physics / factor_lollipop / lollipop | 物理场分析因子棒棒糖（lollipop 模式，合成数据） |
| `physics_field_interval_forest` | physics / interval_forest / interval | 物理场分析区间森林图（interval 模式，合成数据） |
| `physics_field_composition_stream` | physics / composition_stream / stacked-area | 物理场分析组成流面积（stacked-area 模式，合成数据） |
| `physics_field_stage_step` | physics / stage_step / step | 物理场分析阶段阶梯曲线（step 模式，合成数据） |
| `physics_field_surface3d` | physics / surface3d / 3d-surface | 物理场分析三维响应曲面（3d-surface 模式，合成数据） |
| `physics_field_calendar_grid` | physics / calendar_grid / calendar-grid | 物理场分析日历网格（calendar-grid 模式，合成数据） |
| `physics_field_before_after` | physics / before_after / slope | 物理场分析前后斜率对比（slope 模式，合成数据） |
| `physics_field_decision_boundary` | physics / decision_boundary / decision-map | 物理场分析决策边界图（decision-map 模式，合成数据） |
| `synthetic_geo_monitoring` | geo-grid / monitoring / time-band | 合成地理栅格监测带状时序（time-band 模式，合成数据） |
| `synthetic_geo_limit_watch` | geo-grid / limit_watch / control-limit | 合成地理栅格控制限监测（control-limit 模式，合成数据） |
| `synthetic_geo_state_map` | geo-grid / state_map / heatmap | 合成地理栅格状态热力图（heatmap 模式，合成数据） |
| `synthetic_geo_response_surface` | geo-grid / response_surface / contour | 合成地理栅格响应等值面（contour 模式，合成数据） |
| `synthetic_geo_cluster_view` | geo-grid / cluster_view / cluster | 合成地理栅格状态聚类散点（cluster 模式，合成数据） |
| `synthetic_geo_rank_profile` | geo-grid / rank_profile / ranking | 合成地理栅格指标排序条形（ranking 模式，合成数据） |
| `synthetic_geo_score_radar` | geo-grid / score_radar / radar | 合成地理栅格多维评分雷达（radar 模式，合成数据） |
| `synthetic_geo_contribution_bridge` | geo-grid / contribution_bridge / waterfall | 合成地理栅格贡献瀑布桥（waterfall 模式，合成数据） |
| `synthetic_geo_scenario_facets` | geo-grid / scenario_facets / small-multiples | 合成地理栅格场景分面（small-multiples 模式，合成数据） |
| `synthetic_geo_polar_signature` | geo-grid / polar_signature / polar | 合成地理栅格极坐标指纹（polar 模式，合成数据） |
| `synthetic_geo_phase_portrait` | geo-grid / phase_portrait / phase-plane | 合成地理栅格相平面画像（phase-plane 模式，合成数据） |
| `synthetic_geo_distribution_shift` | geo-grid / distribution_shift / distribution | 合成地理栅格分布漂移（distribution 模式，合成数据） |
| `synthetic_geo_interaction_matrix` | geo-grid / interaction_matrix / matrix | 合成地理栅格交互气泡矩阵（matrix 模式，合成数据） |
| `synthetic_geo_factor_lollipop` | geo-grid / factor_lollipop / lollipop | 合成地理栅格因子棒棒糖（lollipop 模式，合成数据） |
| `synthetic_geo_interval_forest` | geo-grid / interval_forest / interval | 合成地理栅格区间森林图（interval 模式，合成数据） |
| `synthetic_geo_composition_stream` | geo-grid / composition_stream / stacked-area | 合成地理栅格组成流面积（stacked-area 模式，合成数据） |
| `synthetic_geo_stage_step` | geo-grid / stage_step / step | 合成地理栅格阶段阶梯曲线（step 模式，合成数据） |
| `synthetic_geo_surface3d` | geo-grid / surface3d / 3d-surface | 合成地理栅格三维响应曲面（3d-surface 模式，合成数据） |
| `synthetic_geo_calendar_grid` | geo-grid / calendar_grid / calendar-grid | 合成地理栅格日历网格（calendar-grid 模式，合成数据） |
| `synthetic_geo_before_after` | geo-grid / before_after / slope | 合成地理栅格前后斜率对比（slope 模式，合成数据） |
| `synthetic_geo_decision_boundary` | geo-grid / decision_boundary / decision-map | 合成地理栅格决策边界图（decision-map 模式，合成数据） |
| `geoscience_grid_monitoring` | geoscience / monitoring / time-band | 地学栅格场监测带状时序（time-band 模式，合成数据） |
| `geoscience_grid_limit_watch` | geoscience / limit_watch / control-limit | 地学栅格场控制限监测（control-limit 模式，合成数据） |
| `geoscience_grid_state_map` | geoscience / state_map / heatmap | 地学栅格场状态热力图（heatmap 模式，合成数据） |
| `geoscience_grid_response_surface` | geoscience / response_surface / contour | 地学栅格场响应等值面（contour 模式，合成数据） |
| `geoscience_grid_cluster_view` | geoscience / cluster_view / cluster | 地学栅格场状态聚类散点（cluster 模式，合成数据） |
| `geoscience_grid_rank_profile` | geoscience / rank_profile / ranking | 地学栅格场指标排序条形（ranking 模式，合成数据） |
| `geoscience_grid_score_radar` | geoscience / score_radar / radar | 地学栅格场多维评分雷达（radar 模式，合成数据） |
| `geoscience_grid_contribution_bridge` | geoscience / contribution_bridge / waterfall | 地学栅格场贡献瀑布桥（waterfall 模式，合成数据） |
| `geoscience_grid_scenario_facets` | geoscience / scenario_facets / small-multiples | 地学栅格场场景分面（small-multiples 模式，合成数据） |
| `geoscience_grid_polar_signature` | geoscience / polar_signature / polar | 地学栅格场极坐标指纹（polar 模式，合成数据） |
| `geoscience_grid_phase_portrait` | geoscience / phase_portrait / phase-plane | 地学栅格场相平面画像（phase-plane 模式，合成数据） |
| `geoscience_grid_distribution_shift` | geoscience / distribution_shift / distribution | 地学栅格场分布漂移（distribution 模式，合成数据） |
| `geoscience_grid_interaction_matrix` | geoscience / interaction_matrix / matrix | 地学栅格场交互气泡矩阵（matrix 模式，合成数据） |
| `geoscience_grid_factor_lollipop` | geoscience / factor_lollipop / lollipop | 地学栅格场因子棒棒糖（lollipop 模式，合成数据） |
| `geoscience_grid_interval_forest` | geoscience / interval_forest / interval | 地学栅格场区间森林图（interval 模式，合成数据） |
| `geoscience_grid_composition_stream` | geoscience / composition_stream / stacked-area | 地学栅格场组成流面积（stacked-area 模式，合成数据） |
| `geoscience_grid_stage_step` | geoscience / stage_step / step | 地学栅格场阶段阶梯曲线（step 模式，合成数据） |
| `geoscience_grid_surface3d` | geoscience / surface3d / 3d-surface | 地学栅格场三维响应曲面（3d-surface 模式，合成数据） |
| `geoscience_grid_calendar_grid` | geoscience / calendar_grid / calendar-grid | 地学栅格场日历网格（calendar-grid 模式，合成数据） |
| `geoscience_grid_before_after` | geoscience / before_after / slope | 地学栅格场前后斜率对比（slope 模式，合成数据） |
| `geoscience_grid_decision_boundary` | geoscience / decision_boundary / decision-map | 地学栅格场决策边界图（decision-map 模式，合成数据） |

## 排名/多维 (ranking)

| 名称 | 标签 | 说明 |
|---|---|---|
| `radar_chart` | radar | 雷达图 |
| `parallel_coordinates` | parallel / multivar | 平行坐标 |
| `waffle_chart` | waffle / proportion | 华夫饼图 |
| `dot_plot_grouped` | dot / group | 分组点图 |
| `bump_chart` | bump / rank / time | 排名变化 bump chart（多对象随时间名次迁移） |

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
| `anomaly_timeline` | anomaly / event / timeline | 异常事件时间轴（多阈值告警区间+事件标注） |
| `candlestick_ohlc` | finance / ohlc / candlestick | OHLC K 线图（随机游走价格+成交量副图） |
| `control_chart_xbar` | spc / xbar / control-chart | X-bar 控制图（均值线+3σ 控制限+越限标注） |
| `cusum_chart` | spc / cusum / drift | CUSUM 控制图（正负累积偏移检测） |
| `decomposition_stl` | decomposition / trend / seasonal | 时间序列分解面板（观测/趋势/季节/残差） |
| `drawdown_curve` | finance / drawdown / risk | 回撤曲线（净值曲线+最大回撤阴影） |
| `event_raster` | raster / event / spike | 多通道事件栅格图（神经放电/告警日志通用） |
| `ewma_chart` | spc / ewma / control-chart | EWMA 控制图（时变控制限+越限点标红） |
| `fan_chart` | forecast / fan / quantile | 扇形预测图（历史序列+分位数渐变带逐步加宽） |
| `horizon_chart` | horizon / band / small-multiple | 地平线图（分层折叠填色 4 序列小多图） |
| `lag_plot_v2` | lag / autocorrelation / scatter | 滞后散点图阵（lag=1..4 四宫格识别自相关衰减） |
| `pacf_plot` | pacf / ar / correlogram | 偏自相关图（Durbin-Levinson 求 PACF+置信带） |
| `range_band_timeseries` | band / range / seasonal | 历史同期最大最小范围带叠加今年曲线 |
| `returns_heatmap` | heatmap / returns / calendar | 年月矩阵月度收益率热力日历 |
| `seasonal_subseries_v2` | seasonal / subseries / facet | 十二月分面季节子序列加月均值线 |
| `spiral_timeseries` | spiral / polar / seasonal | 极坐标时间螺旋按年盘旋颜色编码数值 |
| `step_after_compare` | step / intervention / ci | 干预前后水平段均值与置信带阶梯对比 |
| `waterfall_timeseries` | waterfall / bridge / monthly | 期初到期末月度增减时序瀑布桥 |

## 复合布局 (composite)

| 名称 | 标签 | 说明 |
|---|---|---|
| `zoomed_inset` | inset / zoom | 局部放大插图 |
| `broken_axis` | broken / axis | 折断坐标轴 |
| `dual_yaxis` | dual / axis | 双 Y 轴 |
| `joint_marginal` | joint / marginal | 主散点+边缘直方 |
| `small_multiples` | trellis | 小型多图阵列 |
| `paper_multipanel_monitoring` | multipanel / monitoring / time-band | 论文多面板版式监测带状时序（time-band 模式，合成数据） |
| `paper_multipanel_limit_watch` | multipanel / limit_watch / control-limit | 论文多面板版式控制限监测（control-limit 模式，合成数据） |
| `paper_multipanel_state_map` | multipanel / state_map / heatmap | 论文多面板版式状态热力图（heatmap 模式，合成数据） |
| `paper_multipanel_response_surface` | multipanel / response_surface / contour | 论文多面板版式响应等值面（contour 模式，合成数据） |
| `paper_multipanel_cluster_view` | multipanel / cluster_view / cluster | 论文多面板版式状态聚类散点（cluster 模式，合成数据） |
| `paper_multipanel_rank_profile` | multipanel / rank_profile / ranking | 论文多面板版式指标排序条形（ranking 模式，合成数据） |
| `paper_multipanel_score_radar` | multipanel / score_radar / radar | 论文多面板版式多维评分雷达（radar 模式，合成数据） |
| `paper_multipanel_contribution_bridge` | multipanel / contribution_bridge / waterfall | 论文多面板版式贡献瀑布桥（waterfall 模式，合成数据） |
| `paper_multipanel_scenario_facets` | multipanel / scenario_facets / small-multiples | 论文多面板版式场景分面（small-multiples 模式，合成数据） |
| `paper_multipanel_polar_signature` | multipanel / polar_signature / polar | 论文多面板版式极坐标指纹（polar 模式，合成数据） |
| `paper_multipanel_phase_portrait` | multipanel / phase_portrait / phase-plane | 论文多面板版式相平面画像（phase-plane 模式，合成数据） |
| `paper_multipanel_distribution_shift` | multipanel / distribution_shift / distribution | 论文多面板版式分布漂移（distribution 模式，合成数据） |
| `paper_multipanel_interaction_matrix` | multipanel / interaction_matrix / matrix | 论文多面板版式交互气泡矩阵（matrix 模式，合成数据） |
| `paper_multipanel_factor_lollipop` | multipanel / factor_lollipop / lollipop | 论文多面板版式因子棒棒糖（lollipop 模式，合成数据） |
| `paper_multipanel_interval_forest` | multipanel / interval_forest / interval | 论文多面板版式区间森林图（interval 模式，合成数据） |
| `paper_multipanel_composition_stream` | multipanel / composition_stream / stacked-area | 论文多面板版式组成流面积（stacked-area 模式，合成数据） |
| `paper_multipanel_stage_step` | multipanel / stage_step / step | 论文多面板版式阶段阶梯曲线（step 模式，合成数据） |
| `paper_multipanel_surface3d` | multipanel / surface3d / 3d-surface | 论文多面板版式三维响应曲面（3d-surface 模式，合成数据） |
| `paper_multipanel_calendar_grid` | multipanel / calendar_grid / calendar-grid | 论文多面板版式日历网格（calendar-grid 模式，合成数据） |
| `paper_multipanel_before_after` | multipanel / before_after / slope | 论文多面板版式前后斜率对比（slope 模式，合成数据） |
| `paper_multipanel_decision_boundary` | multipanel / decision_boundary / decision-map | 论文多面板版式决策边界图（decision-map 模式，合成数据） |

## 流图 (flow)

| 名称 | 标签 | 说明 |
|---|---|---|
| `sankey_basic` | sankey | 桑基流图 |
| `chord_diagram` | chord / flow / matrix | 和弦图（流量矩阵外环节点+带宽编码连接） |
| `sankey_multistage` | sankey / stage / band | 三级桑基源中间汇曲线流带 |
| `stream_graph` | stream / themeriver / stacked | 摆动基线堆叠面积河流图 |

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
| `bio_signal_monitoring` | biosignal / monitoring / time-band | 生物信号监测带状时序（time-band 模式，合成数据） |
| `bio_signal_limit_watch` | biosignal / limit_watch / control-limit | 生物信号控制限监测（control-limit 模式，合成数据） |
| `bio_signal_state_map` | biosignal / state_map / heatmap | 生物信号状态热力图（heatmap 模式，合成数据） |
| `bio_signal_response_surface` | biosignal / response_surface / contour | 生物信号响应等值面（contour 模式，合成数据） |
| `bio_signal_cluster_view` | biosignal / cluster_view / cluster | 生物信号状态聚类散点（cluster 模式，合成数据） |
| `bio_signal_rank_profile` | biosignal / rank_profile / ranking | 生物信号指标排序条形（ranking 模式，合成数据） |
| `bio_signal_score_radar` | biosignal / score_radar / radar | 生物信号多维评分雷达（radar 模式，合成数据） |
| `bio_signal_contribution_bridge` | biosignal / contribution_bridge / waterfall | 生物信号贡献瀑布桥（waterfall 模式，合成数据） |
| `bio_signal_scenario_facets` | biosignal / scenario_facets / small-multiples | 生物信号场景分面（small-multiples 模式，合成数据） |
| `bio_signal_polar_signature` | biosignal / polar_signature / polar | 生物信号极坐标指纹（polar 模式，合成数据） |
| `bio_signal_phase_portrait` | biosignal / phase_portrait / phase-plane | 生物信号相平面画像（phase-plane 模式，合成数据） |
| `bio_signal_distribution_shift` | biosignal / distribution_shift / distribution | 生物信号分布漂移（distribution 模式，合成数据） |
| `bio_signal_interaction_matrix` | biosignal / interaction_matrix / matrix | 生物信号交互气泡矩阵（matrix 模式，合成数据） |
| `bio_signal_factor_lollipop` | biosignal / factor_lollipop / lollipop | 生物信号因子棒棒糖（lollipop 模式，合成数据） |
| `bio_signal_interval_forest` | biosignal / interval_forest / interval | 生物信号区间森林图（interval 模式，合成数据） |
| `bio_signal_composition_stream` | biosignal / composition_stream / stacked-area | 生物信号组成流面积（stacked-area 模式，合成数据） |
| `bio_signal_stage_step` | biosignal / stage_step / step | 生物信号阶段阶梯曲线（step 模式，合成数据） |
| `bio_signal_surface3d` | biosignal / surface3d / 3d-surface | 生物信号三维响应曲面（3d-surface 模式，合成数据） |
| `bio_signal_calendar_grid` | biosignal / calendar_grid / calendar-grid | 生物信号日历网格（calendar-grid 模式，合成数据） |
| `bio_signal_before_after` | biosignal / before_after / slope | 生物信号前后斜率对比（slope 模式，合成数据） |
| `bio_signal_decision_boundary` | biosignal / decision_boundary / decision-map | 生物信号决策边界图（decision-map 模式，合成数据） |
| `acoustic_voice_monitoring` | acoustics / monitoring / time-band | 声学与声纹监测带状时序（time-band 模式，合成数据） |
| `acoustic_voice_limit_watch` | acoustics / limit_watch / control-limit | 声学与声纹控制限监测（control-limit 模式，合成数据） |
| `acoustic_voice_state_map` | acoustics / state_map / heatmap | 声学与声纹状态热力图（heatmap 模式，合成数据） |
| `acoustic_voice_response_surface` | acoustics / response_surface / contour | 声学与声纹响应等值面（contour 模式，合成数据） |
| `acoustic_voice_cluster_view` | acoustics / cluster_view / cluster | 声学与声纹状态聚类散点（cluster 模式，合成数据） |
| `acoustic_voice_rank_profile` | acoustics / rank_profile / ranking | 声学与声纹指标排序条形（ranking 模式，合成数据） |
| `acoustic_voice_score_radar` | acoustics / score_radar / radar | 声学与声纹多维评分雷达（radar 模式，合成数据） |
| `acoustic_voice_contribution_bridge` | acoustics / contribution_bridge / waterfall | 声学与声纹贡献瀑布桥（waterfall 模式，合成数据） |
| `acoustic_voice_scenario_facets` | acoustics / scenario_facets / small-multiples | 声学与声纹场景分面（small-multiples 模式，合成数据） |
| `acoustic_voice_polar_signature` | acoustics / polar_signature / polar | 声学与声纹极坐标指纹（polar 模式，合成数据） |
| `acoustic_voice_phase_portrait` | acoustics / phase_portrait / phase-plane | 声学与声纹相平面画像（phase-plane 模式，合成数据） |
| `acoustic_voice_distribution_shift` | acoustics / distribution_shift / distribution | 声学与声纹分布漂移（distribution 模式，合成数据） |
| `acoustic_voice_interaction_matrix` | acoustics / interaction_matrix / matrix | 声学与声纹交互气泡矩阵（matrix 模式，合成数据） |
| `acoustic_voice_factor_lollipop` | acoustics / factor_lollipop / lollipop | 声学与声纹因子棒棒糖（lollipop 模式，合成数据） |
| `acoustic_voice_interval_forest` | acoustics / interval_forest / interval | 声学与声纹区间森林图（interval 模式，合成数据） |
| `acoustic_voice_composition_stream` | acoustics / composition_stream / stacked-area | 声学与声纹组成流面积（stacked-area 模式，合成数据） |
| `acoustic_voice_stage_step` | acoustics / stage_step / step | 声学与声纹阶段阶梯曲线（step 模式，合成数据） |
| `acoustic_voice_surface3d` | acoustics / surface3d / 3d-surface | 声学与声纹三维响应曲面（3d-surface 模式，合成数据） |
| `acoustic_voice_calendar_grid` | acoustics / calendar_grid / calendar-grid | 声学与声纹日历网格（calendar-grid 模式，合成数据） |
| `acoustic_voice_before_after` | acoustics / before_after / slope | 声学与声纹前后斜率对比（slope 模式，合成数据） |
| `acoustic_voice_decision_boundary` | acoustics / decision_boundary / decision-map | 声学与声纹决策边界图（decision-map 模式，合成数据） |

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
| `motor_deep_monitoring` | motor / monitoring / time-band | 电机深化监测带状时序（time-band 模式，合成数据） |
| `motor_deep_limit_watch` | motor / limit_watch / control-limit | 电机深化控制限监测（control-limit 模式，合成数据） |
| `motor_deep_state_map` | motor / state_map / heatmap | 电机深化状态热力图（heatmap 模式，合成数据） |
| `motor_deep_response_surface` | motor / response_surface / contour | 电机深化响应等值面（contour 模式，合成数据） |
| `motor_deep_cluster_view` | motor / cluster_view / cluster | 电机深化状态聚类散点（cluster 模式，合成数据） |
| `motor_deep_rank_profile` | motor / rank_profile / ranking | 电机深化指标排序条形（ranking 模式，合成数据） |
| `motor_deep_score_radar` | motor / score_radar / radar | 电机深化多维评分雷达（radar 模式，合成数据） |
| `motor_deep_contribution_bridge` | motor / contribution_bridge / waterfall | 电机深化贡献瀑布桥（waterfall 模式，合成数据） |
| `motor_deep_scenario_facets` | motor / scenario_facets / small-multiples | 电机深化场景分面（small-multiples 模式，合成数据） |
| `motor_deep_polar_signature` | motor / polar_signature / polar | 电机深化极坐标指纹（polar 模式，合成数据） |
| `motor_deep_phase_portrait` | motor / phase_portrait / phase-plane | 电机深化相平面画像（phase-plane 模式，合成数据） |
| `motor_deep_distribution_shift` | motor / distribution_shift / distribution | 电机深化分布漂移（distribution 模式，合成数据） |
| `motor_deep_interaction_matrix` | motor / interaction_matrix / matrix | 电机深化交互气泡矩阵（matrix 模式，合成数据） |
| `motor_deep_factor_lollipop` | motor / factor_lollipop / lollipop | 电机深化因子棒棒糖（lollipop 模式，合成数据） |
| `motor_deep_interval_forest` | motor / interval_forest / interval | 电机深化区间森林图（interval 模式，合成数据） |
| `motor_deep_composition_stream` | motor / composition_stream / stacked-area | 电机深化组成流面积（stacked-area 模式，合成数据） |
| `motor_deep_stage_step` | motor / stage_step / step | 电机深化阶段阶梯曲线（step 模式，合成数据） |
| `motor_deep_surface3d` | motor / surface3d / 3d-surface | 电机深化三维响应曲面（3d-surface 模式，合成数据） |
| `motor_deep_calendar_grid` | motor / calendar_grid / calendar-grid | 电机深化日历网格（calendar-grid 模式，合成数据） |
| `motor_deep_before_after` | motor / before_after / slope | 电机深化前后斜率对比（slope 模式，合成数据） |
| `motor_deep_decision_boundary` | motor / decision_boundary / decision-map | 电机深化决策边界图（decision-map 模式，合成数据） |
| `instrument_meter_monitoring` | instrumentation / monitoring / time-band | 测量仪表监测带状时序（time-band 模式，合成数据） |
| `instrument_meter_limit_watch` | instrumentation / limit_watch / control-limit | 测量仪表控制限监测（control-limit 模式，合成数据） |
| `instrument_meter_state_map` | instrumentation / state_map / heatmap | 测量仪表状态热力图（heatmap 模式，合成数据） |
| `instrument_meter_response_surface` | instrumentation / response_surface / contour | 测量仪表响应等值面（contour 模式，合成数据） |
| `instrument_meter_cluster_view` | instrumentation / cluster_view / cluster | 测量仪表状态聚类散点（cluster 模式，合成数据） |
| `instrument_meter_rank_profile` | instrumentation / rank_profile / ranking | 测量仪表指标排序条形（ranking 模式，合成数据） |
| `instrument_meter_score_radar` | instrumentation / score_radar / radar | 测量仪表多维评分雷达（radar 模式，合成数据） |
| `instrument_meter_contribution_bridge` | instrumentation / contribution_bridge / waterfall | 测量仪表贡献瀑布桥（waterfall 模式，合成数据） |
| `instrument_meter_scenario_facets` | instrumentation / scenario_facets / small-multiples | 测量仪表场景分面（small-multiples 模式，合成数据） |
| `instrument_meter_polar_signature` | instrumentation / polar_signature / polar | 测量仪表极坐标指纹（polar 模式，合成数据） |
| `instrument_meter_phase_portrait` | instrumentation / phase_portrait / phase-plane | 测量仪表相平面画像（phase-plane 模式，合成数据） |
| `instrument_meter_distribution_shift` | instrumentation / distribution_shift / distribution | 测量仪表分布漂移（distribution 模式，合成数据） |
| `instrument_meter_interaction_matrix` | instrumentation / interaction_matrix / matrix | 测量仪表交互气泡矩阵（matrix 模式，合成数据） |
| `instrument_meter_factor_lollipop` | instrumentation / factor_lollipop / lollipop | 测量仪表因子棒棒糖（lollipop 模式，合成数据） |
| `instrument_meter_interval_forest` | instrumentation / interval_forest / interval | 测量仪表区间森林图（interval 模式，合成数据） |
| `instrument_meter_composition_stream` | instrumentation / composition_stream / stacked-area | 测量仪表组成流面积（stacked-area 模式，合成数据） |
| `instrument_meter_stage_step` | instrumentation / stage_step / step | 测量仪表阶段阶梯曲线（step 模式，合成数据） |
| `instrument_meter_surface3d` | instrumentation / surface3d / 3d-surface | 测量仪表三维响应曲面（3d-surface 模式，合成数据） |
| `instrument_meter_calendar_grid` | instrumentation / calendar_grid / calendar-grid | 测量仪表日历网格（calendar-grid 模式，合成数据） |
| `instrument_meter_before_after` | instrumentation / before_after / slope | 测量仪表前后斜率对比（slope 模式，合成数据） |
| `instrument_meter_decision_boundary` | instrumentation / decision_boundary / decision-map | 测量仪表决策边界图（decision-map 模式，合成数据） |
| `insulation_diagnostics_monitoring` | insulation / monitoring / time-band | 绝缘诊断监测带状时序（time-band 模式，合成数据） |
| `insulation_diagnostics_limit_watch` | insulation / limit_watch / control-limit | 绝缘诊断控制限监测（control-limit 模式，合成数据） |
| `insulation_diagnostics_state_map` | insulation / state_map / heatmap | 绝缘诊断状态热力图（heatmap 模式，合成数据） |
| `insulation_diagnostics_response_surface` | insulation / response_surface / contour | 绝缘诊断响应等值面（contour 模式，合成数据） |
| `insulation_diagnostics_cluster_view` | insulation / cluster_view / cluster | 绝缘诊断状态聚类散点（cluster 模式，合成数据） |
| `insulation_diagnostics_rank_profile` | insulation / rank_profile / ranking | 绝缘诊断指标排序条形（ranking 模式，合成数据） |
| `insulation_diagnostics_score_radar` | insulation / score_radar / radar | 绝缘诊断多维评分雷达（radar 模式，合成数据） |
| `insulation_diagnostics_contribution_bridge` | insulation / contribution_bridge / waterfall | 绝缘诊断贡献瀑布桥（waterfall 模式，合成数据） |
| `insulation_diagnostics_scenario_facets` | insulation / scenario_facets / small-multiples | 绝缘诊断场景分面（small-multiples 模式，合成数据） |
| `insulation_diagnostics_polar_signature` | insulation / polar_signature / polar | 绝缘诊断极坐标指纹（polar 模式，合成数据） |
| `insulation_diagnostics_phase_portrait` | insulation / phase_portrait / phase-plane | 绝缘诊断相平面画像（phase-plane 模式，合成数据） |
| `insulation_diagnostics_distribution_shift` | insulation / distribution_shift / distribution | 绝缘诊断分布漂移（distribution 模式，合成数据） |
| `insulation_diagnostics_interaction_matrix` | insulation / interaction_matrix / matrix | 绝缘诊断交互气泡矩阵（matrix 模式，合成数据） |
| `insulation_diagnostics_factor_lollipop` | insulation / factor_lollipop / lollipop | 绝缘诊断因子棒棒糖（lollipop 模式，合成数据） |
| `insulation_diagnostics_interval_forest` | insulation / interval_forest / interval | 绝缘诊断区间森林图（interval 模式，合成数据） |
| `insulation_diagnostics_composition_stream` | insulation / composition_stream / stacked-area | 绝缘诊断组成流面积（stacked-area 模式，合成数据） |
| `insulation_diagnostics_stage_step` | insulation / stage_step / step | 绝缘诊断阶段阶梯曲线（step 模式，合成数据） |
| `insulation_diagnostics_surface3d` | insulation / surface3d / 3d-surface | 绝缘诊断三维响应曲面（3d-surface 模式，合成数据） |
| `insulation_diagnostics_calendar_grid` | insulation / calendar_grid / calendar-grid | 绝缘诊断日历网格（calendar-grid 模式，合成数据） |
| `insulation_diagnostics_before_after` | insulation / before_after / slope | 绝缘诊断前后斜率对比（slope 模式，合成数据） |
| `insulation_diagnostics_decision_boundary` | insulation / decision_boundary / decision-map | 绝缘诊断决策边界图（decision-map 模式，合成数据） |

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
| `control_mpc_monitoring` | mpc / monitoring / time-band | MPC 控制进阶监测带状时序（time-band 模式，合成数据） |
| `control_mpc_limit_watch` | mpc / limit_watch / control-limit | MPC 控制进阶控制限监测（control-limit 模式，合成数据） |
| `control_mpc_state_map` | mpc / state_map / heatmap | MPC 控制进阶状态热力图（heatmap 模式，合成数据） |
| `control_mpc_response_surface` | mpc / response_surface / contour | MPC 控制进阶响应等值面（contour 模式，合成数据） |
| `control_mpc_cluster_view` | mpc / cluster_view / cluster | MPC 控制进阶状态聚类散点（cluster 模式，合成数据） |
| `control_mpc_rank_profile` | mpc / rank_profile / ranking | MPC 控制进阶指标排序条形（ranking 模式，合成数据） |
| `control_mpc_score_radar` | mpc / score_radar / radar | MPC 控制进阶多维评分雷达（radar 模式，合成数据） |
| `control_mpc_contribution_bridge` | mpc / contribution_bridge / waterfall | MPC 控制进阶贡献瀑布桥（waterfall 模式，合成数据） |
| `control_mpc_scenario_facets` | mpc / scenario_facets / small-multiples | MPC 控制进阶场景分面（small-multiples 模式，合成数据） |
| `control_mpc_polar_signature` | mpc / polar_signature / polar | MPC 控制进阶极坐标指纹（polar 模式，合成数据） |
| `control_mpc_phase_portrait` | mpc / phase_portrait / phase-plane | MPC 控制进阶相平面画像（phase-plane 模式，合成数据） |
| `control_mpc_distribution_shift` | mpc / distribution_shift / distribution | MPC 控制进阶分布漂移（distribution 模式，合成数据） |
| `control_mpc_interaction_matrix` | mpc / interaction_matrix / matrix | MPC 控制进阶交互气泡矩阵（matrix 模式，合成数据） |
| `control_mpc_factor_lollipop` | mpc / factor_lollipop / lollipop | MPC 控制进阶因子棒棒糖（lollipop 模式，合成数据） |
| `control_mpc_interval_forest` | mpc / interval_forest / interval | MPC 控制进阶区间森林图（interval 模式，合成数据） |
| `control_mpc_composition_stream` | mpc / composition_stream / stacked-area | MPC 控制进阶组成流面积（stacked-area 模式，合成数据） |
| `control_mpc_stage_step` | mpc / stage_step / step | MPC 控制进阶阶段阶梯曲线（step 模式，合成数据） |
| `control_mpc_surface3d` | mpc / surface3d / 3d-surface | MPC 控制进阶三维响应曲面（3d-surface 模式，合成数据） |
| `control_mpc_calendar_grid` | mpc / calendar_grid / calendar-grid | MPC 控制进阶日历网格（calendar-grid 模式，合成数据） |
| `control_mpc_before_after` | mpc / before_after / slope | MPC 控制进阶前后斜率对比（slope 模式，合成数据） |
| `control_mpc_decision_boundary` | mpc / decision_boundary / decision-map | MPC 控制进阶决策边界图（decision-map 模式，合成数据） |
| `observer_estimation_monitoring` | observer / monitoring / time-band | 观测器与状态估计监测带状时序（time-band 模式，合成数据） |
| `observer_estimation_limit_watch` | observer / limit_watch / control-limit | 观测器与状态估计控制限监测（control-limit 模式，合成数据） |
| `observer_estimation_state_map` | observer / state_map / heatmap | 观测器与状态估计状态热力图（heatmap 模式，合成数据） |
| `observer_estimation_response_surface` | observer / response_surface / contour | 观测器与状态估计响应等值面（contour 模式，合成数据） |
| `observer_estimation_cluster_view` | observer / cluster_view / cluster | 观测器与状态估计状态聚类散点（cluster 模式，合成数据） |
| `observer_estimation_rank_profile` | observer / rank_profile / ranking | 观测器与状态估计指标排序条形（ranking 模式，合成数据） |
| `observer_estimation_score_radar` | observer / score_radar / radar | 观测器与状态估计多维评分雷达（radar 模式，合成数据） |
| `observer_estimation_contribution_bridge` | observer / contribution_bridge / waterfall | 观测器与状态估计贡献瀑布桥（waterfall 模式，合成数据） |
| `observer_estimation_scenario_facets` | observer / scenario_facets / small-multiples | 观测器与状态估计场景分面（small-multiples 模式，合成数据） |
| `observer_estimation_polar_signature` | observer / polar_signature / polar | 观测器与状态估计极坐标指纹（polar 模式，合成数据） |
| `observer_estimation_phase_portrait` | observer / phase_portrait / phase-plane | 观测器与状态估计相平面画像（phase-plane 模式，合成数据） |
| `observer_estimation_distribution_shift` | observer / distribution_shift / distribution | 观测器与状态估计分布漂移（distribution 模式，合成数据） |
| `observer_estimation_interaction_matrix` | observer / interaction_matrix / matrix | 观测器与状态估计交互气泡矩阵（matrix 模式，合成数据） |
| `observer_estimation_factor_lollipop` | observer / factor_lollipop / lollipop | 观测器与状态估计因子棒棒糖（lollipop 模式，合成数据） |
| `observer_estimation_interval_forest` | observer / interval_forest / interval | 观测器与状态估计区间森林图（interval 模式，合成数据） |
| `observer_estimation_composition_stream` | observer / composition_stream / stacked-area | 观测器与状态估计组成流面积（stacked-area 模式，合成数据） |
| `observer_estimation_stage_step` | observer / stage_step / step | 观测器与状态估计阶段阶梯曲线（step 模式，合成数据） |
| `observer_estimation_surface3d` | observer / surface3d / 3d-surface | 观测器与状态估计三维响应曲面（3d-surface 模式，合成数据） |
| `observer_estimation_calendar_grid` | observer / calendar_grid / calendar-grid | 观测器与状态估计日历网格（calendar-grid 模式，合成数据） |
| `observer_estimation_before_after` | observer / before_after / slope | 观测器与状态估计前后斜率对比（slope 模式，合成数据） |
| `observer_estimation_decision_boundary` | observer / decision_boundary / decision-map | 观测器与状态估计决策边界图（decision-map 模式，合成数据） |

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
| `antenna_pattern_3d_v2` | antenna / 3d / array-factor | 三维天线方向图（阵列方向因子曲面） |
| `array_factor_polar` | array / beam / polar | 均匀线阵方向因子极坐标图 |
| `beam_steering` | beamforming / steering / array | 波束扫描方向图（多角度主瓣偏转对比） |
| `ber_waterfall_3d` | ber / waterfall / snr | BER 瀑布曲面（调制阶数×SNR×误码率） |
| `eye_diagram_v2` | eye / raised-cosine / isi | 升余弦脉冲眼图（噪声+ISI 多迹叠加） |
| `qam_constellation_grid` | QAM / constellation / EVM | 4/16/64/256-QAM 星座四宫格含 EVM 标注 |
| `radar_advanced_monitoring` | radar / monitoring / time-band | 雷达进阶监测带状时序（time-band 模式，合成数据） |
| `radar_advanced_limit_watch` | radar / limit_watch / control-limit | 雷达进阶控制限监测（control-limit 模式，合成数据） |
| `radar_advanced_state_map` | radar / state_map / heatmap | 雷达进阶状态热力图（heatmap 模式，合成数据） |
| `radar_advanced_response_surface` | radar / response_surface / contour | 雷达进阶响应等值面（contour 模式，合成数据） |
| `radar_advanced_cluster_view` | radar / cluster_view / cluster | 雷达进阶状态聚类散点（cluster 模式，合成数据） |
| `radar_advanced_rank_profile` | radar / rank_profile / ranking | 雷达进阶指标排序条形（ranking 模式，合成数据） |
| `radar_advanced_score_radar` | radar / score_radar / radar | 雷达进阶多维评分雷达（radar 模式，合成数据） |
| `radar_advanced_contribution_bridge` | radar / contribution_bridge / waterfall | 雷达进阶贡献瀑布桥（waterfall 模式，合成数据） |
| `radar_advanced_scenario_facets` | radar / scenario_facets / small-multiples | 雷达进阶场景分面（small-multiples 模式，合成数据） |
| `radar_advanced_polar_signature` | radar / polar_signature / polar | 雷达进阶极坐标指纹（polar 模式，合成数据） |
| `radar_advanced_phase_portrait` | radar / phase_portrait / phase-plane | 雷达进阶相平面画像（phase-plane 模式，合成数据） |
| `radar_advanced_distribution_shift` | radar / distribution_shift / distribution | 雷达进阶分布漂移（distribution 模式，合成数据） |
| `radar_advanced_interaction_matrix` | radar / interaction_matrix / matrix | 雷达进阶交互气泡矩阵（matrix 模式，合成数据） |
| `radar_advanced_factor_lollipop` | radar / factor_lollipop / lollipop | 雷达进阶因子棒棒糖（lollipop 模式，合成数据） |
| `radar_advanced_interval_forest` | radar / interval_forest / interval | 雷达进阶区间森林图（interval 模式，合成数据） |
| `radar_advanced_composition_stream` | radar / composition_stream / stacked-area | 雷达进阶组成流面积（stacked-area 模式，合成数据） |
| `radar_advanced_stage_step` | radar / stage_step / step | 雷达进阶阶段阶梯曲线（step 模式，合成数据） |
| `radar_advanced_surface3d` | radar / surface3d / 3d-surface | 雷达进阶三维响应曲面（3d-surface 模式，合成数据） |
| `radar_advanced_calendar_grid` | radar / calendar_grid / calendar-grid | 雷达进阶日历网格（calendar-grid 模式，合成数据） |
| `radar_advanced_before_after` | radar / before_after / slope | 雷达进阶前后斜率对比（slope 模式，合成数据） |
| `radar_advanced_decision_boundary` | radar / decision_boundary / decision-map | 雷达进阶决策边界图（decision-map 模式，合成数据） |
| `antenna_array_monitoring` | antenna / monitoring / time-band | 天线阵列监测带状时序（time-band 模式，合成数据） |
| `antenna_array_limit_watch` | antenna / limit_watch / control-limit | 天线阵列控制限监测（control-limit 模式，合成数据） |
| `antenna_array_state_map` | antenna / state_map / heatmap | 天线阵列状态热力图（heatmap 模式，合成数据） |
| `antenna_array_response_surface` | antenna / response_surface / contour | 天线阵列响应等值面（contour 模式，合成数据） |
| `antenna_array_cluster_view` | antenna / cluster_view / cluster | 天线阵列状态聚类散点（cluster 模式，合成数据） |
| `antenna_array_rank_profile` | antenna / rank_profile / ranking | 天线阵列指标排序条形（ranking 模式，合成数据） |
| `antenna_array_score_radar` | antenna / score_radar / radar | 天线阵列多维评分雷达（radar 模式，合成数据） |
| `antenna_array_contribution_bridge` | antenna / contribution_bridge / waterfall | 天线阵列贡献瀑布桥（waterfall 模式，合成数据） |
| `antenna_array_scenario_facets` | antenna / scenario_facets / small-multiples | 天线阵列场景分面（small-multiples 模式，合成数据） |
| `antenna_array_polar_signature` | antenna / polar_signature / polar | 天线阵列极坐标指纹（polar 模式，合成数据） |
| `antenna_array_phase_portrait` | antenna / phase_portrait / phase-plane | 天线阵列相平面画像（phase-plane 模式，合成数据） |
| `antenna_array_distribution_shift` | antenna / distribution_shift / distribution | 天线阵列分布漂移（distribution 模式，合成数据） |
| `antenna_array_interaction_matrix` | antenna / interaction_matrix / matrix | 天线阵列交互气泡矩阵（matrix 模式，合成数据） |
| `antenna_array_factor_lollipop` | antenna / factor_lollipop / lollipop | 天线阵列因子棒棒糖（lollipop 模式，合成数据） |
| `antenna_array_interval_forest` | antenna / interval_forest / interval | 天线阵列区间森林图（interval 模式，合成数据） |
| `antenna_array_composition_stream` | antenna / composition_stream / stacked-area | 天线阵列组成流面积（stacked-area 模式，合成数据） |
| `antenna_array_stage_step` | antenna / stage_step / step | 天线阵列阶段阶梯曲线（step 模式，合成数据） |
| `antenna_array_surface3d` | antenna / surface3d / 3d-surface | 天线阵列三维响应曲面（3d-surface 模式，合成数据） |
| `antenna_array_calendar_grid` | antenna / calendar_grid / calendar-grid | 天线阵列日历网格（calendar-grid 模式，合成数据） |
| `antenna_array_before_after` | antenna / before_after / slope | 天线阵列前后斜率对比（slope 模式，合成数据） |
| `antenna_array_decision_boundary` | antenna / decision_boundary / decision-map | 天线阵列决策边界图（decision-map 模式，合成数据） |

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
| `ml_explain_monitoring` | xai / monitoring / time-band | 机器学习可解释性监测带状时序（time-band 模式，合成数据） |
| `ml_explain_limit_watch` | xai / limit_watch / control-limit | 机器学习可解释性控制限监测（control-limit 模式，合成数据） |
| `ml_explain_state_map` | xai / state_map / heatmap | 机器学习可解释性状态热力图（heatmap 模式，合成数据） |
| `ml_explain_response_surface` | xai / response_surface / contour | 机器学习可解释性响应等值面（contour 模式，合成数据） |
| `ml_explain_cluster_view` | xai / cluster_view / cluster | 机器学习可解释性状态聚类散点（cluster 模式，合成数据） |
| `ml_explain_rank_profile` | xai / rank_profile / ranking | 机器学习可解释性指标排序条形（ranking 模式，合成数据） |
| `ml_explain_score_radar` | xai / score_radar / radar | 机器学习可解释性多维评分雷达（radar 模式，合成数据） |
| `ml_explain_contribution_bridge` | xai / contribution_bridge / waterfall | 机器学习可解释性贡献瀑布桥（waterfall 模式，合成数据） |
| `ml_explain_scenario_facets` | xai / scenario_facets / small-multiples | 机器学习可解释性场景分面（small-multiples 模式，合成数据） |
| `ml_explain_polar_signature` | xai / polar_signature / polar | 机器学习可解释性极坐标指纹（polar 模式，合成数据） |
| `ml_explain_phase_portrait` | xai / phase_portrait / phase-plane | 机器学习可解释性相平面画像（phase-plane 模式，合成数据） |
| `ml_explain_distribution_shift` | xai / distribution_shift / distribution | 机器学习可解释性分布漂移（distribution 模式，合成数据） |
| `ml_explain_interaction_matrix` | xai / interaction_matrix / matrix | 机器学习可解释性交互气泡矩阵（matrix 模式，合成数据） |
| `ml_explain_factor_lollipop` | xai / factor_lollipop / lollipop | 机器学习可解释性因子棒棒糖（lollipop 模式，合成数据） |
| `ml_explain_interval_forest` | xai / interval_forest / interval | 机器学习可解释性区间森林图（interval 模式，合成数据） |
| `ml_explain_composition_stream` | xai / composition_stream / stacked-area | 机器学习可解释性组成流面积（stacked-area 模式，合成数据） |
| `ml_explain_stage_step` | xai / stage_step / step | 机器学习可解释性阶段阶梯曲线（step 模式，合成数据） |
| `ml_explain_surface3d` | xai / surface3d / 3d-surface | 机器学习可解释性三维响应曲面（3d-surface 模式，合成数据） |
| `ml_explain_calendar_grid` | xai / calendar_grid / calendar-grid | 机器学习可解释性日历网格（calendar-grid 模式，合成数据） |
| `ml_explain_before_after` | xai / before_after / slope | 机器学习可解释性前后斜率对比（slope 模式，合成数据） |
| `ml_explain_decision_boundary` | xai / decision_boundary / decision-map | 机器学习可解释性决策边界图（decision-map 模式，合成数据） |
| `model_diagnostics_monitoring` | diagnostics / monitoring / time-band | 模型诊断监测带状时序（time-band 模式，合成数据） |
| `model_diagnostics_limit_watch` | diagnostics / limit_watch / control-limit | 模型诊断控制限监测（control-limit 模式，合成数据） |
| `model_diagnostics_state_map` | diagnostics / state_map / heatmap | 模型诊断状态热力图（heatmap 模式，合成数据） |
| `model_diagnostics_response_surface` | diagnostics / response_surface / contour | 模型诊断响应等值面（contour 模式，合成数据） |
| `model_diagnostics_cluster_view` | diagnostics / cluster_view / cluster | 模型诊断状态聚类散点（cluster 模式，合成数据） |
| `model_diagnostics_rank_profile` | diagnostics / rank_profile / ranking | 模型诊断指标排序条形（ranking 模式，合成数据） |
| `model_diagnostics_score_radar` | diagnostics / score_radar / radar | 模型诊断多维评分雷达（radar 模式，合成数据） |
| `model_diagnostics_contribution_bridge` | diagnostics / contribution_bridge / waterfall | 模型诊断贡献瀑布桥（waterfall 模式，合成数据） |
| `model_diagnostics_scenario_facets` | diagnostics / scenario_facets / small-multiples | 模型诊断场景分面（small-multiples 模式，合成数据） |
| `model_diagnostics_polar_signature` | diagnostics / polar_signature / polar | 模型诊断极坐标指纹（polar 模式，合成数据） |
| `model_diagnostics_phase_portrait` | diagnostics / phase_portrait / phase-plane | 模型诊断相平面画像（phase-plane 模式，合成数据） |
| `model_diagnostics_distribution_shift` | diagnostics / distribution_shift / distribution | 模型诊断分布漂移（distribution 模式，合成数据） |
| `model_diagnostics_interaction_matrix` | diagnostics / interaction_matrix / matrix | 模型诊断交互气泡矩阵（matrix 模式，合成数据） |
| `model_diagnostics_factor_lollipop` | diagnostics / factor_lollipop / lollipop | 模型诊断因子棒棒糖（lollipop 模式，合成数据） |
| `model_diagnostics_interval_forest` | diagnostics / interval_forest / interval | 模型诊断区间森林图（interval 模式，合成数据） |
| `model_diagnostics_composition_stream` | diagnostics / composition_stream / stacked-area | 模型诊断组成流面积（stacked-area 模式，合成数据） |
| `model_diagnostics_stage_step` | diagnostics / stage_step / step | 模型诊断阶段阶梯曲线（step 模式，合成数据） |
| `model_diagnostics_surface3d` | diagnostics / surface3d / 3d-surface | 模型诊断三维响应曲面（3d-surface 模式，合成数据） |
| `model_diagnostics_calendar_grid` | diagnostics / calendar_grid / calendar-grid | 模型诊断日历网格（calendar-grid 模式，合成数据） |
| `model_diagnostics_before_after` | diagnostics / before_after / slope | 模型诊断前后斜率对比（slope 模式，合成数据） |
| `model_diagnostics_decision_boundary` | diagnostics / decision_boundary / decision-map | 模型诊断决策边界图（decision-map 模式，合成数据） |

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
| `materials_microstructure_monitoring` | materials / monitoring / time-band | 材料微结构监测带状时序（time-band 模式，合成数据） |
| `materials_microstructure_limit_watch` | materials / limit_watch / control-limit | 材料微结构控制限监测（control-limit 模式，合成数据） |
| `materials_microstructure_state_map` | materials / state_map / heatmap | 材料微结构状态热力图（heatmap 模式，合成数据） |
| `materials_microstructure_response_surface` | materials / response_surface / contour | 材料微结构响应等值面（contour 模式，合成数据） |
| `materials_microstructure_cluster_view` | materials / cluster_view / cluster | 材料微结构状态聚类散点（cluster 模式，合成数据） |
| `materials_microstructure_rank_profile` | materials / rank_profile / ranking | 材料微结构指标排序条形（ranking 模式，合成数据） |
| `materials_microstructure_score_radar` | materials / score_radar / radar | 材料微结构多维评分雷达（radar 模式，合成数据） |
| `materials_microstructure_contribution_bridge` | materials / contribution_bridge / waterfall | 材料微结构贡献瀑布桥（waterfall 模式，合成数据） |
| `materials_microstructure_scenario_facets` | materials / scenario_facets / small-multiples | 材料微结构场景分面（small-multiples 模式，合成数据） |
| `materials_microstructure_polar_signature` | materials / polar_signature / polar | 材料微结构极坐标指纹（polar 模式，合成数据） |
| `materials_microstructure_phase_portrait` | materials / phase_portrait / phase-plane | 材料微结构相平面画像（phase-plane 模式，合成数据） |
| `materials_microstructure_distribution_shift` | materials / distribution_shift / distribution | 材料微结构分布漂移（distribution 模式，合成数据） |
| `materials_microstructure_interaction_matrix` | materials / interaction_matrix / matrix | 材料微结构交互气泡矩阵（matrix 模式，合成数据） |
| `materials_microstructure_factor_lollipop` | materials / factor_lollipop / lollipop | 材料微结构因子棒棒糖（lollipop 模式，合成数据） |
| `materials_microstructure_interval_forest` | materials / interval_forest / interval | 材料微结构区间森林图（interval 模式，合成数据） |
| `materials_microstructure_composition_stream` | materials / composition_stream / stacked-area | 材料微结构组成流面积（stacked-area 模式，合成数据） |
| `materials_microstructure_stage_step` | materials / stage_step / step | 材料微结构阶段阶梯曲线（step 模式，合成数据） |
| `materials_microstructure_surface3d` | materials / surface3d / 3d-surface | 材料微结构三维响应曲面（3d-surface 模式，合成数据） |
| `materials_microstructure_calendar_grid` | materials / calendar_grid / calendar-grid | 材料微结构日历网格（calendar-grid 模式，合成数据） |
| `materials_microstructure_before_after` | materials / before_after / slope | 材料微结构前后斜率对比（slope 模式，合成数据） |
| `materials_microstructure_decision_boundary` | materials / decision_boundary / decision-map | 材料微结构决策边界图（decision-map 模式，合成数据） |
| `chemistry_spectra_monitoring` | chemistry / monitoring / time-band | 化学谱图监测带状时序（time-band 模式，合成数据） |
| `chemistry_spectra_limit_watch` | chemistry / limit_watch / control-limit | 化学谱图控制限监测（control-limit 模式，合成数据） |
| `chemistry_spectra_state_map` | chemistry / state_map / heatmap | 化学谱图状态热力图（heatmap 模式，合成数据） |
| `chemistry_spectra_response_surface` | chemistry / response_surface / contour | 化学谱图响应等值面（contour 模式，合成数据） |
| `chemistry_spectra_cluster_view` | chemistry / cluster_view / cluster | 化学谱图状态聚类散点（cluster 模式，合成数据） |
| `chemistry_spectra_rank_profile` | chemistry / rank_profile / ranking | 化学谱图指标排序条形（ranking 模式，合成数据） |
| `chemistry_spectra_score_radar` | chemistry / score_radar / radar | 化学谱图多维评分雷达（radar 模式，合成数据） |
| `chemistry_spectra_contribution_bridge` | chemistry / contribution_bridge / waterfall | 化学谱图贡献瀑布桥（waterfall 模式，合成数据） |
| `chemistry_spectra_scenario_facets` | chemistry / scenario_facets / small-multiples | 化学谱图场景分面（small-multiples 模式，合成数据） |
| `chemistry_spectra_polar_signature` | chemistry / polar_signature / polar | 化学谱图极坐标指纹（polar 模式，合成数据） |
| `chemistry_spectra_phase_portrait` | chemistry / phase_portrait / phase-plane | 化学谱图相平面画像（phase-plane 模式，合成数据） |
| `chemistry_spectra_distribution_shift` | chemistry / distribution_shift / distribution | 化学谱图分布漂移（distribution 模式，合成数据） |
| `chemistry_spectra_interaction_matrix` | chemistry / interaction_matrix / matrix | 化学谱图交互气泡矩阵（matrix 模式，合成数据） |
| `chemistry_spectra_factor_lollipop` | chemistry / factor_lollipop / lollipop | 化学谱图因子棒棒糖（lollipop 模式，合成数据） |
| `chemistry_spectra_interval_forest` | chemistry / interval_forest / interval | 化学谱图区间森林图（interval 模式，合成数据） |
| `chemistry_spectra_composition_stream` | chemistry / composition_stream / stacked-area | 化学谱图组成流面积（stacked-area 模式，合成数据） |
| `chemistry_spectra_stage_step` | chemistry / stage_step / step | 化学谱图阶段阶梯曲线（step 模式，合成数据） |
| `chemistry_spectra_surface3d` | chemistry / surface3d / 3d-surface | 化学谱图三维响应曲面（3d-surface 模式，合成数据） |
| `chemistry_spectra_calendar_grid` | chemistry / calendar_grid / calendar-grid | 化学谱图日历网格（calendar-grid 模式，合成数据） |
| `chemistry_spectra_before_after` | chemistry / before_after / slope | 化学谱图前后斜率对比（slope 模式，合成数据） |
| `chemistry_spectra_decision_boundary` | chemistry / decision_boundary / decision-map | 化学谱图决策边界图（decision-map 模式，合成数据） |
| `quantum_semiconductor_monitoring` | semiconductor / monitoring / time-band | 量子与半导体监测带状时序（time-band 模式，合成数据） |
| `quantum_semiconductor_limit_watch` | semiconductor / limit_watch / control-limit | 量子与半导体控制限监测（control-limit 模式，合成数据） |
| `quantum_semiconductor_state_map` | semiconductor / state_map / heatmap | 量子与半导体状态热力图（heatmap 模式，合成数据） |
| `quantum_semiconductor_response_surface` | semiconductor / response_surface / contour | 量子与半导体响应等值面（contour 模式，合成数据） |
| `quantum_semiconductor_cluster_view` | semiconductor / cluster_view / cluster | 量子与半导体状态聚类散点（cluster 模式，合成数据） |
| `quantum_semiconductor_rank_profile` | semiconductor / rank_profile / ranking | 量子与半导体指标排序条形（ranking 模式，合成数据） |
| `quantum_semiconductor_score_radar` | semiconductor / score_radar / radar | 量子与半导体多维评分雷达（radar 模式，合成数据） |
| `quantum_semiconductor_contribution_bridge` | semiconductor / contribution_bridge / waterfall | 量子与半导体贡献瀑布桥（waterfall 模式，合成数据） |
| `quantum_semiconductor_scenario_facets` | semiconductor / scenario_facets / small-multiples | 量子与半导体场景分面（small-multiples 模式，合成数据） |
| `quantum_semiconductor_polar_signature` | semiconductor / polar_signature / polar | 量子与半导体极坐标指纹（polar 模式，合成数据） |
| `quantum_semiconductor_phase_portrait` | semiconductor / phase_portrait / phase-plane | 量子与半导体相平面画像（phase-plane 模式，合成数据） |
| `quantum_semiconductor_distribution_shift` | semiconductor / distribution_shift / distribution | 量子与半导体分布漂移（distribution 模式，合成数据） |
| `quantum_semiconductor_interaction_matrix` | semiconductor / interaction_matrix / matrix | 量子与半导体交互气泡矩阵（matrix 模式，合成数据） |
| `quantum_semiconductor_factor_lollipop` | semiconductor / factor_lollipop / lollipop | 量子与半导体因子棒棒糖（lollipop 模式，合成数据） |
| `quantum_semiconductor_interval_forest` | semiconductor / interval_forest / interval | 量子与半导体区间森林图（interval 模式，合成数据） |
| `quantum_semiconductor_composition_stream` | semiconductor / composition_stream / stacked-area | 量子与半导体组成流面积（stacked-area 模式，合成数据） |
| `quantum_semiconductor_stage_step` | semiconductor / stage_step / step | 量子与半导体阶段阶梯曲线（step 模式，合成数据） |
| `quantum_semiconductor_surface3d` | semiconductor / surface3d / 3d-surface | 量子与半导体三维响应曲面（3d-surface 模式，合成数据） |
| `quantum_semiconductor_calendar_grid` | semiconductor / calendar_grid / calendar-grid | 量子与半导体日历网格（calendar-grid 模式，合成数据） |
| `quantum_semiconductor_before_after` | semiconductor / before_after / slope | 量子与半导体前后斜率对比（slope 模式，合成数据） |
| `quantum_semiconductor_decision_boundary` | semiconductor / decision_boundary / decision-map | 量子与半导体决策边界图（decision-map 模式，合成数据） |

## CFD/流体 (cfd)

| 名称 | 标签 | 说明 |
|---|---|---|
| `velocity_field_cfd` | velocity / quiver | CFD 速度场+矢量箭头 |
| `pressure_contour` | pressure / contour | 压力等高线（圆柱绕流） |
| `vorticity_map` | vorticity | 涡量场 |
| `streamlines_colored` | streamlines | 按速度模值着色流线 |
| `residual_history` | residual / iteration | CFD 迭代残差曲线 |
| `thermal_system_monitoring` | thermal / monitoring / time-band | 热学系统监测带状时序（time-band 模式，合成数据） |
| `thermal_system_limit_watch` | thermal / limit_watch / control-limit | 热学系统控制限监测（control-limit 模式，合成数据） |
| `thermal_system_state_map` | thermal / state_map / heatmap | 热学系统状态热力图（heatmap 模式，合成数据） |
| `thermal_system_response_surface` | thermal / response_surface / contour | 热学系统响应等值面（contour 模式，合成数据） |
| `thermal_system_cluster_view` | thermal / cluster_view / cluster | 热学系统状态聚类散点（cluster 模式，合成数据） |
| `thermal_system_rank_profile` | thermal / rank_profile / ranking | 热学系统指标排序条形（ranking 模式，合成数据） |
| `thermal_system_score_radar` | thermal / score_radar / radar | 热学系统多维评分雷达（radar 模式，合成数据） |
| `thermal_system_contribution_bridge` | thermal / contribution_bridge / waterfall | 热学系统贡献瀑布桥（waterfall 模式，合成数据） |
| `thermal_system_scenario_facets` | thermal / scenario_facets / small-multiples | 热学系统场景分面（small-multiples 模式，合成数据） |
| `thermal_system_polar_signature` | thermal / polar_signature / polar | 热学系统极坐标指纹（polar 模式，合成数据） |
| `thermal_system_phase_portrait` | thermal / phase_portrait / phase-plane | 热学系统相平面画像（phase-plane 模式，合成数据） |
| `thermal_system_distribution_shift` | thermal / distribution_shift / distribution | 热学系统分布漂移（distribution 模式，合成数据） |
| `thermal_system_interaction_matrix` | thermal / interaction_matrix / matrix | 热学系统交互气泡矩阵（matrix 模式，合成数据） |
| `thermal_system_factor_lollipop` | thermal / factor_lollipop / lollipop | 热学系统因子棒棒糖（lollipop 模式，合成数据） |
| `thermal_system_interval_forest` | thermal / interval_forest / interval | 热学系统区间森林图（interval 模式，合成数据） |
| `thermal_system_composition_stream` | thermal / composition_stream / stacked-area | 热学系统组成流面积（stacked-area 模式，合成数据） |
| `thermal_system_stage_step` | thermal / stage_step / step | 热学系统阶段阶梯曲线（step 模式，合成数据） |
| `thermal_system_surface3d` | thermal / surface3d / 3d-surface | 热学系统三维响应曲面（3d-surface 模式，合成数据） |
| `thermal_system_calendar_grid` | thermal / calendar_grid / calendar-grid | 热学系统日历网格（calendar-grid 模式，合成数据） |
| `thermal_system_before_after` | thermal / before_after / slope | 热学系统前后斜率对比（slope 模式，合成数据） |
| `thermal_system_decision_boundary` | thermal / decision_boundary / decision-map | 热学系统决策边界图（decision-map 模式，合成数据） |
| `fluid_cfd_monitoring` | fluid / monitoring / time-band | 流体与 CFD监测带状时序（time-band 模式，合成数据） |
| `fluid_cfd_limit_watch` | fluid / limit_watch / control-limit | 流体与 CFD控制限监测（control-limit 模式，合成数据） |
| `fluid_cfd_state_map` | fluid / state_map / heatmap | 流体与 CFD状态热力图（heatmap 模式，合成数据） |
| `fluid_cfd_response_surface` | fluid / response_surface / contour | 流体与 CFD响应等值面（contour 模式，合成数据） |
| `fluid_cfd_cluster_view` | fluid / cluster_view / cluster | 流体与 CFD状态聚类散点（cluster 模式，合成数据） |
| `fluid_cfd_rank_profile` | fluid / rank_profile / ranking | 流体与 CFD指标排序条形（ranking 模式，合成数据） |
| `fluid_cfd_score_radar` | fluid / score_radar / radar | 流体与 CFD多维评分雷达（radar 模式，合成数据） |
| `fluid_cfd_contribution_bridge` | fluid / contribution_bridge / waterfall | 流体与 CFD贡献瀑布桥（waterfall 模式，合成数据） |
| `fluid_cfd_scenario_facets` | fluid / scenario_facets / small-multiples | 流体与 CFD场景分面（small-multiples 模式，合成数据） |
| `fluid_cfd_polar_signature` | fluid / polar_signature / polar | 流体与 CFD极坐标指纹（polar 模式，合成数据） |
| `fluid_cfd_phase_portrait` | fluid / phase_portrait / phase-plane | 流体与 CFD相平面画像（phase-plane 模式，合成数据） |
| `fluid_cfd_distribution_shift` | fluid / distribution_shift / distribution | 流体与 CFD分布漂移（distribution 模式，合成数据） |
| `fluid_cfd_interaction_matrix` | fluid / interaction_matrix / matrix | 流体与 CFD交互气泡矩阵（matrix 模式，合成数据） |
| `fluid_cfd_factor_lollipop` | fluid / factor_lollipop / lollipop | 流体与 CFD因子棒棒糖（lollipop 模式，合成数据） |
| `fluid_cfd_interval_forest` | fluid / interval_forest / interval | 流体与 CFD区间森林图（interval 模式，合成数据） |
| `fluid_cfd_composition_stream` | fluid / composition_stream / stacked-area | 流体与 CFD组成流面积（stacked-area 模式，合成数据） |
| `fluid_cfd_stage_step` | fluid / stage_step / step | 流体与 CFD阶段阶梯曲线（step 模式，合成数据） |
| `fluid_cfd_surface3d` | fluid / surface3d / 3d-surface | 流体与 CFD三维响应曲面（3d-surface 模式，合成数据） |
| `fluid_cfd_calendar_grid` | fluid / calendar_grid / calendar-grid | 流体与 CFD日历网格（calendar-grid 模式，合成数据） |
| `fluid_cfd_before_after` | fluid / before_after / slope | 流体与 CFD前后斜率对比（slope 模式，合成数据） |
| `fluid_cfd_decision_boundary` | fluid / decision_boundary / decision-map | 流体与 CFD决策边界图（decision-map 模式，合成数据） |

## 优化算法 (optimization)

| 名称 | 标签 | 说明 |
|---|---|---|
| `convergence_curve` | loss / convergence | 多算法收敛对比 |
| `pareto_front` | pareto / multiobj | Pareto 前沿 |
| `fitness_landscape` | landscape / population | 适应度地形 |
| `ga_evolution` | GA / fitness | GA 适应度演化 |
| `gradient_descent_path` | gradient / path | 梯度下降路径 |
| `optimization_viz_monitoring` | optimization / monitoring / time-band | 优化算法可视化监测带状时序（time-band 模式，合成数据） |
| `optimization_viz_limit_watch` | optimization / limit_watch / control-limit | 优化算法可视化控制限监测（control-limit 模式，合成数据） |
| `optimization_viz_state_map` | optimization / state_map / heatmap | 优化算法可视化状态热力图（heatmap 模式，合成数据） |
| `optimization_viz_response_surface` | optimization / response_surface / contour | 优化算法可视化响应等值面（contour 模式，合成数据） |
| `optimization_viz_cluster_view` | optimization / cluster_view / cluster | 优化算法可视化状态聚类散点（cluster 模式，合成数据） |
| `optimization_viz_rank_profile` | optimization / rank_profile / ranking | 优化算法可视化指标排序条形（ranking 模式，合成数据） |
| `optimization_viz_score_radar` | optimization / score_radar / radar | 优化算法可视化多维评分雷达（radar 模式，合成数据） |
| `optimization_viz_contribution_bridge` | optimization / contribution_bridge / waterfall | 优化算法可视化贡献瀑布桥（waterfall 模式，合成数据） |
| `optimization_viz_scenario_facets` | optimization / scenario_facets / small-multiples | 优化算法可视化场景分面（small-multiples 模式，合成数据） |
| `optimization_viz_polar_signature` | optimization / polar_signature / polar | 优化算法可视化极坐标指纹（polar 模式，合成数据） |
| `optimization_viz_phase_portrait` | optimization / phase_portrait / phase-plane | 优化算法可视化相平面画像（phase-plane 模式，合成数据） |
| `optimization_viz_distribution_shift` | optimization / distribution_shift / distribution | 优化算法可视化分布漂移（distribution 模式，合成数据） |
| `optimization_viz_interaction_matrix` | optimization / interaction_matrix / matrix | 优化算法可视化交互气泡矩阵（matrix 模式，合成数据） |
| `optimization_viz_factor_lollipop` | optimization / factor_lollipop / lollipop | 优化算法可视化因子棒棒糖（lollipop 模式，合成数据） |
| `optimization_viz_interval_forest` | optimization / interval_forest / interval | 优化算法可视化区间森林图（interval 模式，合成数据） |
| `optimization_viz_composition_stream` | optimization / composition_stream / stacked-area | 优化算法可视化组成流面积（stacked-area 模式，合成数据） |
| `optimization_viz_stage_step` | optimization / stage_step / step | 优化算法可视化阶段阶梯曲线（step 模式，合成数据） |
| `optimization_viz_surface3d` | optimization / surface3d / 3d-surface | 优化算法可视化三维响应曲面（3d-surface 模式，合成数据） |
| `optimization_viz_calendar_grid` | optimization / calendar_grid / calendar-grid | 优化算法可视化日历网格（calendar-grid 模式，合成数据） |
| `optimization_viz_before_after` | optimization / before_after / slope | 优化算法可视化前后斜率对比（slope 模式，合成数据） |
| `optimization_viz_decision_boundary` | optimization / decision_boundary / decision-map | 优化算法可视化决策边界图（decision-map 模式，合成数据） |

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
| `harmonic_heatmap` | harmonic / heatmap / time-varying | 谐波时变热力图（谐波次数×时间幅值着色） |
| `interharmonic_spectrum` | interharmonic / harmonic / spectrum | 间谐波频谱（整数次谐波与间谐波分色柱状） |
| `itic_tolerance_curve` | itic / cbema / voltage-sag | ITIC/CBEMA 电压耐受曲线（半对数包络+事件分区着色） |
| `pq_radar` | radar / quality / thd | 电能质量五维雷达多场景对比 |
| `unbalance_phasor` | phasor / sequence / unbalance | 三相不平衡正负零序相量分解 |
| `voltage_flicker` | flicker / pst / quality | 电压闪变调幅波形与 Pst 条形双面板 |
| `power_system_deep_monitoring` | grid / monitoring / time-band | 电力系统深化监测带状时序（time-band 模式，合成数据） |
| `power_system_deep_limit_watch` | grid / limit_watch / control-limit | 电力系统深化控制限监测（control-limit 模式，合成数据） |
| `power_system_deep_state_map` | grid / state_map / heatmap | 电力系统深化状态热力图（heatmap 模式，合成数据） |
| `power_system_deep_response_surface` | grid / response_surface / contour | 电力系统深化响应等值面（contour 模式，合成数据） |
| `power_system_deep_cluster_view` | grid / cluster_view / cluster | 电力系统深化状态聚类散点（cluster 模式，合成数据） |
| `power_system_deep_rank_profile` | grid / rank_profile / ranking | 电力系统深化指标排序条形（ranking 模式，合成数据） |
| `power_system_deep_score_radar` | grid / score_radar / radar | 电力系统深化多维评分雷达（radar 模式，合成数据） |
| `power_system_deep_contribution_bridge` | grid / contribution_bridge / waterfall | 电力系统深化贡献瀑布桥（waterfall 模式，合成数据） |
| `power_system_deep_scenario_facets` | grid / scenario_facets / small-multiples | 电力系统深化场景分面（small-multiples 模式，合成数据） |
| `power_system_deep_polar_signature` | grid / polar_signature / polar | 电力系统深化极坐标指纹（polar 模式，合成数据） |
| `power_system_deep_phase_portrait` | grid / phase_portrait / phase-plane | 电力系统深化相平面画像（phase-plane 模式，合成数据） |
| `power_system_deep_distribution_shift` | grid / distribution_shift / distribution | 电力系统深化分布漂移（distribution 模式，合成数据） |
| `power_system_deep_interaction_matrix` | grid / interaction_matrix / matrix | 电力系统深化交互气泡矩阵（matrix 模式，合成数据） |
| `power_system_deep_factor_lollipop` | grid / factor_lollipop / lollipop | 电力系统深化因子棒棒糖（lollipop 模式，合成数据） |
| `power_system_deep_interval_forest` | grid / interval_forest / interval | 电力系统深化区间森林图（interval 模式，合成数据） |
| `power_system_deep_composition_stream` | grid / composition_stream / stacked-area | 电力系统深化组成流面积（stacked-area 模式，合成数据） |
| `power_system_deep_stage_step` | grid / stage_step / step | 电力系统深化阶段阶梯曲线（step 模式，合成数据） |
| `power_system_deep_surface3d` | grid / surface3d / 3d-surface | 电力系统深化三维响应曲面（3d-surface 模式，合成数据） |
| `power_system_deep_calendar_grid` | grid / calendar_grid / calendar-grid | 电力系统深化日历网格（calendar-grid 模式，合成数据） |
| `power_system_deep_before_after` | grid / before_after / slope | 电力系统深化前后斜率对比（slope 模式，合成数据） |
| `power_system_deep_decision_boundary` | grid / decision_boundary / decision-map | 电力系统深化决策边界图（decision-map 模式，合成数据） |
| `hvdc_facts_monitoring` | hvdc / monitoring / time-band | HVDC 与 FACTS监测带状时序（time-band 模式，合成数据） |
| `hvdc_facts_limit_watch` | hvdc / limit_watch / control-limit | HVDC 与 FACTS控制限监测（control-limit 模式，合成数据） |
| `hvdc_facts_state_map` | hvdc / state_map / heatmap | HVDC 与 FACTS状态热力图（heatmap 模式，合成数据） |
| `hvdc_facts_response_surface` | hvdc / response_surface / contour | HVDC 与 FACTS响应等值面（contour 模式，合成数据） |
| `hvdc_facts_cluster_view` | hvdc / cluster_view / cluster | HVDC 与 FACTS状态聚类散点（cluster 模式，合成数据） |
| `hvdc_facts_rank_profile` | hvdc / rank_profile / ranking | HVDC 与 FACTS指标排序条形（ranking 模式，合成数据） |
| `hvdc_facts_score_radar` | hvdc / score_radar / radar | HVDC 与 FACTS多维评分雷达（radar 模式，合成数据） |
| `hvdc_facts_contribution_bridge` | hvdc / contribution_bridge / waterfall | HVDC 与 FACTS贡献瀑布桥（waterfall 模式，合成数据） |
| `hvdc_facts_scenario_facets` | hvdc / scenario_facets / small-multiples | HVDC 与 FACTS场景分面（small-multiples 模式，合成数据） |
| `hvdc_facts_polar_signature` | hvdc / polar_signature / polar | HVDC 与 FACTS极坐标指纹（polar 模式，合成数据） |
| `hvdc_facts_phase_portrait` | hvdc / phase_portrait / phase-plane | HVDC 与 FACTS相平面画像（phase-plane 模式，合成数据） |
| `hvdc_facts_distribution_shift` | hvdc / distribution_shift / distribution | HVDC 与 FACTS分布漂移（distribution 模式，合成数据） |
| `hvdc_facts_interaction_matrix` | hvdc / interaction_matrix / matrix | HVDC 与 FACTS交互气泡矩阵（matrix 模式，合成数据） |
| `hvdc_facts_factor_lollipop` | hvdc / factor_lollipop / lollipop | HVDC 与 FACTS因子棒棒糖（lollipop 模式，合成数据） |
| `hvdc_facts_interval_forest` | hvdc / interval_forest / interval | HVDC 与 FACTS区间森林图（interval 模式，合成数据） |
| `hvdc_facts_composition_stream` | hvdc / composition_stream / stacked-area | HVDC 与 FACTS组成流面积（stacked-area 模式，合成数据） |
| `hvdc_facts_stage_step` | hvdc / stage_step / step | HVDC 与 FACTS阶段阶梯曲线（step 模式，合成数据） |
| `hvdc_facts_surface3d` | hvdc / surface3d / 3d-surface | HVDC 与 FACTS三维响应曲面（3d-surface 模式，合成数据） |
| `hvdc_facts_calendar_grid` | hvdc / calendar_grid / calendar-grid | HVDC 与 FACTS日历网格（calendar-grid 模式，合成数据） |
| `hvdc_facts_before_after` | hvdc / before_after / slope | HVDC 与 FACTS前后斜率对比（slope 模式，合成数据） |
| `hvdc_facts_decision_boundary` | hvdc / decision_boundary / decision-map | HVDC 与 FACTS决策边界图（decision-map 模式，合成数据） |
| `protection_fault_monitoring` | protection / monitoring / time-band | 保护与故障分析监测带状时序（time-band 模式，合成数据） |
| `protection_fault_limit_watch` | protection / limit_watch / control-limit | 保护与故障分析控制限监测（control-limit 模式，合成数据） |
| `protection_fault_state_map` | protection / state_map / heatmap | 保护与故障分析状态热力图（heatmap 模式，合成数据） |
| `protection_fault_response_surface` | protection / response_surface / contour | 保护与故障分析响应等值面（contour 模式，合成数据） |
| `protection_fault_cluster_view` | protection / cluster_view / cluster | 保护与故障分析状态聚类散点（cluster 模式，合成数据） |
| `protection_fault_rank_profile` | protection / rank_profile / ranking | 保护与故障分析指标排序条形（ranking 模式，合成数据） |
| `protection_fault_score_radar` | protection / score_radar / radar | 保护与故障分析多维评分雷达（radar 模式，合成数据） |
| `protection_fault_contribution_bridge` | protection / contribution_bridge / waterfall | 保护与故障分析贡献瀑布桥（waterfall 模式，合成数据） |
| `protection_fault_scenario_facets` | protection / scenario_facets / small-multiples | 保护与故障分析场景分面（small-multiples 模式，合成数据） |
| `protection_fault_polar_signature` | protection / polar_signature / polar | 保护与故障分析极坐标指纹（polar 模式，合成数据） |
| `protection_fault_phase_portrait` | protection / phase_portrait / phase-plane | 保护与故障分析相平面画像（phase-plane 模式，合成数据） |
| `protection_fault_distribution_shift` | protection / distribution_shift / distribution | 保护与故障分析分布漂移（distribution 模式，合成数据） |
| `protection_fault_interaction_matrix` | protection / interaction_matrix / matrix | 保护与故障分析交互气泡矩阵（matrix 模式，合成数据） |
| `protection_fault_factor_lollipop` | protection / factor_lollipop / lollipop | 保护与故障分析因子棒棒糖（lollipop 模式，合成数据） |
| `protection_fault_interval_forest` | protection / interval_forest / interval | 保护与故障分析区间森林图（interval 模式，合成数据） |
| `protection_fault_composition_stream` | protection / composition_stream / stacked-area | 保护与故障分析组成流面积（stacked-area 模式，合成数据） |
| `protection_fault_stage_step` | protection / stage_step / step | 保护与故障分析阶段阶梯曲线（step 模式，合成数据） |
| `protection_fault_surface3d` | protection / surface3d / 3d-surface | 保护与故障分析三维响应曲面（3d-surface 模式，合成数据） |
| `protection_fault_calendar_grid` | protection / calendar_grid / calendar-grid | 保护与故障分析日历网格（calendar-grid 模式，合成数据） |
| `protection_fault_before_after` | protection / before_after / slope | 保护与故障分析前后斜率对比（slope 模式，合成数据） |
| `protection_fault_decision_boundary` | protection / decision_boundary / decision-map | 保护与故障分析决策边界图（decision-map 模式，合成数据） |

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
| `storage_battery_monitoring` | storage / monitoring / time-band | 储能与电池监测带状时序（time-band 模式，合成数据） |
| `storage_battery_limit_watch` | storage / limit_watch / control-limit | 储能与电池控制限监测（control-limit 模式，合成数据） |
| `storage_battery_state_map` | storage / state_map / heatmap | 储能与电池状态热力图（heatmap 模式，合成数据） |
| `storage_battery_response_surface` | storage / response_surface / contour | 储能与电池响应等值面（contour 模式，合成数据） |
| `storage_battery_cluster_view` | storage / cluster_view / cluster | 储能与电池状态聚类散点（cluster 模式，合成数据） |
| `storage_battery_rank_profile` | storage / rank_profile / ranking | 储能与电池指标排序条形（ranking 模式，合成数据） |
| `storage_battery_score_radar` | storage / score_radar / radar | 储能与电池多维评分雷达（radar 模式，合成数据） |
| `storage_battery_contribution_bridge` | storage / contribution_bridge / waterfall | 储能与电池贡献瀑布桥（waterfall 模式，合成数据） |
| `storage_battery_scenario_facets` | storage / scenario_facets / small-multiples | 储能与电池场景分面（small-multiples 模式，合成数据） |
| `storage_battery_polar_signature` | storage / polar_signature / polar | 储能与电池极坐标指纹（polar 模式，合成数据） |
| `storage_battery_phase_portrait` | storage / phase_portrait / phase-plane | 储能与电池相平面画像（phase-plane 模式，合成数据） |
| `storage_battery_distribution_shift` | storage / distribution_shift / distribution | 储能与电池分布漂移（distribution 模式，合成数据） |
| `storage_battery_interaction_matrix` | storage / interaction_matrix / matrix | 储能与电池交互气泡矩阵（matrix 模式，合成数据） |
| `storage_battery_factor_lollipop` | storage / factor_lollipop / lollipop | 储能与电池因子棒棒糖（lollipop 模式，合成数据） |
| `storage_battery_interval_forest` | storage / interval_forest / interval | 储能与电池区间森林图（interval 模式，合成数据） |
| `storage_battery_composition_stream` | storage / composition_stream / stacked-area | 储能与电池组成流面积（stacked-area 模式，合成数据） |
| `storage_battery_stage_step` | storage / stage_step / step | 储能与电池阶段阶梯曲线（step 模式，合成数据） |
| `storage_battery_surface3d` | storage / surface3d / 3d-surface | 储能与电池三维响应曲面（3d-surface 模式，合成数据） |
| `storage_battery_calendar_grid` | storage / calendar_grid / calendar-grid | 储能与电池日历网格（calendar-grid 模式，合成数据） |
| `storage_battery_before_after` | storage / before_after / slope | 储能与电池前后斜率对比（slope 模式，合成数据） |
| `storage_battery_decision_boundary` | storage / decision_boundary / decision-map | 储能与电池决策边界图（decision-map 模式，合成数据） |
| `microgrid_market_monitoring` | microgrid / monitoring / time-band | 微电网与市场监测带状时序（time-band 模式，合成数据） |
| `microgrid_market_limit_watch` | microgrid / limit_watch / control-limit | 微电网与市场控制限监测（control-limit 模式，合成数据） |
| `microgrid_market_state_map` | microgrid / state_map / heatmap | 微电网与市场状态热力图（heatmap 模式，合成数据） |
| `microgrid_market_response_surface` | microgrid / response_surface / contour | 微电网与市场响应等值面（contour 模式，合成数据） |
| `microgrid_market_cluster_view` | microgrid / cluster_view / cluster | 微电网与市场状态聚类散点（cluster 模式，合成数据） |
| `microgrid_market_rank_profile` | microgrid / rank_profile / ranking | 微电网与市场指标排序条形（ranking 模式，合成数据） |
| `microgrid_market_score_radar` | microgrid / score_radar / radar | 微电网与市场多维评分雷达（radar 模式，合成数据） |
| `microgrid_market_contribution_bridge` | microgrid / contribution_bridge / waterfall | 微电网与市场贡献瀑布桥（waterfall 模式，合成数据） |
| `microgrid_market_scenario_facets` | microgrid / scenario_facets / small-multiples | 微电网与市场场景分面（small-multiples 模式，合成数据） |
| `microgrid_market_polar_signature` | microgrid / polar_signature / polar | 微电网与市场极坐标指纹（polar 模式，合成数据） |
| `microgrid_market_phase_portrait` | microgrid / phase_portrait / phase-plane | 微电网与市场相平面画像（phase-plane 模式，合成数据） |
| `microgrid_market_distribution_shift` | microgrid / distribution_shift / distribution | 微电网与市场分布漂移（distribution 模式，合成数据） |
| `microgrid_market_interaction_matrix` | microgrid / interaction_matrix / matrix | 微电网与市场交互气泡矩阵（matrix 模式，合成数据） |
| `microgrid_market_factor_lollipop` | microgrid / factor_lollipop / lollipop | 微电网与市场因子棒棒糖（lollipop 模式，合成数据） |
| `microgrid_market_interval_forest` | microgrid / interval_forest / interval | 微电网与市场区间森林图（interval 模式，合成数据） |
| `microgrid_market_composition_stream` | microgrid / composition_stream / stacked-area | 微电网与市场组成流面积（stacked-area 模式，合成数据） |
| `microgrid_market_stage_step` | microgrid / stage_step / step | 微电网与市场阶段阶梯曲线（step 模式，合成数据） |
| `microgrid_market_surface3d` | microgrid / surface3d / 3d-surface | 微电网与市场三维响应曲面（3d-surface 模式，合成数据） |
| `microgrid_market_calendar_grid` | microgrid / calendar_grid / calendar-grid | 微电网与市场日历网格（calendar-grid 模式，合成数据） |
| `microgrid_market_before_after` | microgrid / before_after / slope | 微电网与市场前后斜率对比（slope 模式，合成数据） |
| `microgrid_market_decision_boundary` | microgrid / decision_boundary / decision-map | 微电网与市场决策边界图（decision-map 模式，合成数据） |

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
| `gantt_chart` | gantt / schedule / project | 甘特图（依赖箭头+今日线+完成度填充） |
| `milestone_timeline` | milestone / timeline / roadmap | 里程碑时间轴（水平主轴标注上下交替防重叠） |
| `education_diagram_monitoring` | education / monitoring / time-band | 教学图解监测带状时序（time-band 模式，合成数据） |
| `education_diagram_limit_watch` | education / limit_watch / control-limit | 教学图解控制限监测（control-limit 模式，合成数据） |
| `education_diagram_state_map` | education / state_map / heatmap | 教学图解状态热力图（heatmap 模式，合成数据） |
| `education_diagram_response_surface` | education / response_surface / contour | 教学图解响应等值面（contour 模式，合成数据） |
| `education_diagram_cluster_view` | education / cluster_view / cluster | 教学图解状态聚类散点（cluster 模式，合成数据） |
| `education_diagram_rank_profile` | education / rank_profile / ranking | 教学图解指标排序条形（ranking 模式，合成数据） |
| `education_diagram_score_radar` | education / score_radar / radar | 教学图解多维评分雷达（radar 模式，合成数据） |
| `education_diagram_contribution_bridge` | education / contribution_bridge / waterfall | 教学图解贡献瀑布桥（waterfall 模式，合成数据） |
| `education_diagram_scenario_facets` | education / scenario_facets / small-multiples | 教学图解场景分面（small-multiples 模式，合成数据） |
| `education_diagram_polar_signature` | education / polar_signature / polar | 教学图解极坐标指纹（polar 模式，合成数据） |
| `education_diagram_phase_portrait` | education / phase_portrait / phase-plane | 教学图解相平面画像（phase-plane 模式，合成数据） |
| `education_diagram_distribution_shift` | education / distribution_shift / distribution | 教学图解分布漂移（distribution 模式，合成数据） |
| `education_diagram_interaction_matrix` | education / interaction_matrix / matrix | 教学图解交互气泡矩阵（matrix 模式，合成数据） |
| `education_diagram_factor_lollipop` | education / factor_lollipop / lollipop | 教学图解因子棒棒糖（lollipop 模式，合成数据） |
| `education_diagram_interval_forest` | education / interval_forest / interval | 教学图解区间森林图（interval 模式，合成数据） |
| `education_diagram_composition_stream` | education / composition_stream / stacked-area | 教学图解组成流面积（stacked-area 模式，合成数据） |
| `education_diagram_stage_step` | education / stage_step / step | 教学图解阶段阶梯曲线（step 模式，合成数据） |
| `education_diagram_surface3d` | education / surface3d / 3d-surface | 教学图解三维响应曲面（3d-surface 模式，合成数据） |
| `education_diagram_calendar_grid` | education / calendar_grid / calendar-grid | 教学图解日历网格（calendar-grid 模式，合成数据） |
| `education_diagram_before_after` | education / before_after / slope | 教学图解前后斜率对比（slope 模式，合成数据） |
| `education_diagram_decision_boundary` | education / decision_boundary / decision-map | 教学图解决策边界图（decision-map 模式，合成数据） |