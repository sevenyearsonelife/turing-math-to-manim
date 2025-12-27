# uv run run_pipeline_demo.py

import os
import sys
from pathlib import Path


def _ensure_project_root_on_path() -> Path:
    """将项目根目录加入 sys.path，便于从 src 导入。"""
    root = Path(__file__).resolve().parents[1]
    if str(root) not in sys.path:
        sys.path.append(str(root))
    return root


def main() -> None:
    _ensure_project_root_on_path()

    if not os.getenv("ANTHROPIC_API_KEY"):
        env_path = Path(__file__).with_name(".env")
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if line.startswith("ANTHROPIC_API_KEY="):
                    value = line.split("=", 1)[1].strip().strip('"').strip("'")
                    if value:
                        os.environ.setdefault("ANTHROPIC_API_KEY", value)
                    break

    if not os.getenv("ANTHROPIC_API_KEY"):
        raise RuntimeError("请先设置 ANTHROPIC_API_KEY 环境变量")

    from src.agents.orchestrator import ReverseKnowledgeTreeOrchestrator

    prompt = "给出三角形变为圆的可视化"

    orchestrator = ReverseKnowledgeTreeOrchestrator(
        max_tree_depth=3,
        enable_code_generation=True,
        enable_threejs_generation=False,
        enable_atlas=False,
    )

    result = orchestrator.process(user_input=prompt, output_dir="output")

    print("\n=== Manim 代码预览（前 400 字）===\n")
    if result.manim_code:
        print(result.manim_code[:400])


if __name__ == "__main__":
    main()
