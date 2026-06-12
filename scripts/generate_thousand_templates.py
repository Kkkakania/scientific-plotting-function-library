#!/usr/bin/env python3
"""Generate the 1000-template expansion wrappers.

This script creates S4-S35 batch manifests plus Python/MATLAB wrappers. The
rendering logic is intentionally centralized in _utils/*/generated_* so the
large expansion remains maintainable and auditable.
"""
from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PY_DIR = ROOT / "templates" / "python"
M_DIR = ROOT / "templates" / "matlab"
BATCH_DIR = ROOT / "_batch_manifests"


CONCEPTS = [
    ("monitoring", "监测带状时序", "monitoring band time series", "band_timeseries"),
    ("limit_watch", "控制限监测", "control limit watch", "control_limit"),
    ("state_map", "状态热力图", "state heatmap", "heatmap"),
    ("response_surface", "响应等值面", "response contour surface", "contour"),
    ("cluster_view", "状态聚类散点", "state cluster scatter", "scatter_cluster"),
    ("rank_profile", "指标排序条形", "ranked metric profile", "rank_bar"),
    ("score_radar", "多维评分雷达", "multi-metric radar", "radar"),
    ("contribution_bridge", "贡献瀑布桥", "contribution waterfall", "waterfall"),
    ("scenario_facets", "场景分面", "scenario small multiples", "small_multiples"),
    ("polar_signature", "极坐标指纹", "polar signature", "polar_profile"),
    ("phase_portrait", "相平面画像", "phase portrait", "phase_plane"),
    ("distribution_shift", "分布漂移", "distribution shift", "distribution"),
    ("interaction_matrix", "交互气泡矩阵", "interaction bubble matrix", "bubble_matrix"),
    ("factor_lollipop", "因子棒棒糖", "factor lollipop", "lollipop"),
    ("interval_forest", "区间森林图", "interval forest", "interval_forest"),
    ("composition_stream", "组成流面积", "composition stream", "stacked_area"),
    ("stage_step", "阶段阶梯曲线", "stage step curve", "step_curve"),
    ("surface3d", "三维响应曲面", "3D response surface", "surface3d"),
    ("calendar_grid", "日历网格", "calendar grid", "calendar_grid"),
    ("before_after", "前后斜率对比", "before-after slope", "slope"),
    ("decision_boundary", "决策边界图", "decision boundary", "decision_map"),
]


PACKS = [
    ("ml_explain", "机器学习可解释性", "machine learning explainability", "ml", "xai"),
    ("model_diagnostics", "模型诊断", "model diagnostics", "ml", "diagnostics"),
    ("control_mpc", "MPC 控制进阶", "advanced MPC control", "control", "mpc"),
    ("observer_estimation", "观测器与状态估计", "observer and state estimation", "control", "observer"),
    ("materials_microstructure", "材料微结构", "materials microstructure", "specialty", "materials"),
    ("chemistry_spectra", "化学谱图", "chemistry spectra", "specialty", "chemistry"),
    ("physics_field", "物理场分析", "physics field analysis", "field", "physics"),
    ("synthetic_geo", "合成地理栅格", "synthetic geospatial grid", "field", "geo-grid"),
    ("paper_multipanel", "论文多面板版式", "paper multipanel layout", "composite", "multipanel"),
    ("motor_deep", "电机深化", "electric motor analysis", "electrical", "motor"),
    ("storage_battery", "储能与电池", "storage and battery analysis", "energy", "storage"),
    ("thermal_system", "热学系统", "thermal system analysis", "cfd", "thermal"),
    ("fluid_cfd", "流体与 CFD", "fluid and CFD analysis", "cfd", "fluid"),
    ("bio_signal", "生物信号", "biomedical signal analysis", "signal", "biosignal"),
    ("instrument_meter", "测量仪表", "instrument and metering", "electrical", "instrumentation"),
    ("optimization_viz", "优化算法可视化", "optimization visualization", "optimization", "optimization"),
    ("quantum_semiconductor", "量子与半导体", "quantum and semiconductor analysis", "specialty", "semiconductor"),
    ("acoustic_voice", "声学与声纹", "acoustic and voice analysis", "signal", "acoustics"),
    ("education_diagram", "教学图解", "educational diagramming", "diagram", "education"),
    ("reliability_maintenance", "可靠性与维修", "reliability and maintenance", "statistical", "reliability"),
    ("logistics_network", "物流与网络", "logistics and network analysis", "relation", "logistics"),
    ("epidemic_model", "传播动力学", "epidemic dynamics", "statistical", "epidemic"),
    ("power_system_deep", "电力系统深化", "power system analysis", "power", "grid"),
    ("hvdc_facts", "HVDC 与 FACTS", "HVDC and FACTS analysis", "power", "hvdc"),
    ("microgrid_market", "微电网与市场", "microgrid and market analysis", "energy", "microgrid"),
    ("insulation_diagnostics", "绝缘诊断", "insulation diagnostics", "electrical", "insulation"),
    ("protection_fault", "保护与故障分析", "protection and fault analysis", "power", "protection"),
    ("radar_advanced", "雷达进阶", "advanced radar analysis", "rf", "radar"),
    ("antenna_array", "天线阵列", "antenna array analysis", "rf", "antenna"),
    ("bayes_uq", "贝叶斯与不确定性量化", "Bayesian uncertainty quantification", "statistical", "bayesian"),
    ("matrix_tensor", "矩阵与张量可视化", "matrix and tensor visualization", "matrix", "tensor"),
    ("geoscience_grid", "地学栅格场", "geoscience grid analysis", "field", "geoscience"),
]


KIND_TAG = {
    "band_timeseries": "time-band",
    "control_limit": "control-limit",
    "heatmap": "heatmap",
    "contour": "contour",
    "scatter_cluster": "cluster",
    "rank_bar": "ranking",
    "radar": "radar",
    "waterfall": "waterfall",
    "small_multiples": "small-multiples",
    "polar_profile": "polar",
    "phase_plane": "phase-plane",
    "distribution": "distribution",
    "bubble_matrix": "matrix",
    "lollipop": "lollipop",
    "interval_forest": "interval",
    "stacked_area": "stacked-area",
    "step_curve": "step",
    "surface3d": "3d-surface",
    "calendar_grid": "calendar-grid",
    "slope": "slope",
    "decision_map": "decision-map",
}


def py_wrapper(name: str, desc: str, kind: str, seed: int, domain: str, topic: str) -> str:
    return f'''"""{name}: {desc}."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '_utils', 'python'))
from generated_patterns import make_template_figure


def make_figure(title='{domain}: {topic}'):
    return make_template_figure('{kind}', seed={seed}, title=title, domain='{domain}', topic='{topic}')


if __name__ == '__main__':
    fig = make_figure()
    fig.savefig(__file__.replace('.py', '.png'), dpi=150)
'''


def matlab_wrapper(name: str, kind: str, seed: int, domain: str, topic: str) -> str:
    return f"""function fig = {name}()
    addpath(fullfile(fileparts(mfilename('fullpath')),'..','..','_utils','matlab'));
    fig = generated_template_figure('{kind}', {seed}, '{domain}: {topic}', '{domain}', '{topic}');
end
"""


def main() -> int:
    BATCH_DIR.mkdir(exist_ok=True)
    written = 0

    for pack_index, (pack_slug, zh_domain, en_domain, category, tag) in enumerate(PACKS, start=4):
        rows: list[str] = []
        for concept_index, (concept_slug, zh_topic, en_topic, kind) in enumerate(CONCEPTS, start=1):
            name = f"{pack_slug}_{concept_slug}"
            desc = f"{zh_domain}{zh_topic}（{KIND_TAG[kind]} 模式，合成数据）"
            tags = f"{tag},{concept_slug},{KIND_TAG[kind]}"
            rows.append(f"{name}|{category}|{tags}|{desc}")
            seed = 1000 + pack_index * 100 + concept_index
            (PY_DIR / f"{name}.py").write_text(
                py_wrapper(name, desc, kind, seed, en_domain, en_topic),
                encoding="utf-8",
            )
            (M_DIR / f"{name}.m").write_text(
                matlab_wrapper(name, kind, seed, en_domain, en_topic),
                encoding="utf-8",
            )
            written += 1
        (BATCH_DIR / f"batch_S{pack_index}.txt").write_text("\n".join(rows) + "\n", encoding="utf-8")

    print(f"wrote {written} generated template pairs and {len(PACKS)} batch manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
