#!/bin/bash
# 一键 MATLAB 全库实跑验证（macOS / Linux）
# 用法： bash scripts/verify_matlab.sh            # 全部 274 个
#        bash scripts/verify_matlab.sh bode_diagram swing_curve   # 指定模板
set -e
cd "$(dirname "$0")/.."

# 自动定位 MATLAB CLI：先 PATH，再 /Applications 里最新版本
MATLAB_BIN="$(command -v matlab || true)"
if [ -z "$MATLAB_BIN" ]; then
  MATLAB_BIN="$(ls -d /Applications/MATLAB_R*.app/bin/matlab 2>/dev/null | sort | tail -1 || true)"
fi
if [ -z "$MATLAB_BIN" ]; then
  echo "未找到 MATLAB。请把 matlab 加入 PATH，或安装在 /Applications/MATLAB_R20xx.app"
  echo "（把 alias matlab=\"/Applications/MATLAB_R20xx.app/bin/matlab\" 加进 ~/.zshrc 即可）"
  exit 1
fi
echo "使用: $MATLAB_BIN"

if [ $# -eq 0 ]; then
  "$MATLAB_BIN" -batch "addpath('scripts'); verify_matlab"
else
  LIST=$(printf "'%s'," "$@"); LIST="{${LIST%,}}"
  "$MATLAB_BIN" -batch "addpath('scripts'); verify_matlab($LIST)"
fi
echo "报告: docs/matlab_verify_report.md   渲染图: gallery/matlab/"
