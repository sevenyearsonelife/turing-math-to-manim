# Math-To-Manim

<div align="center">

<!-- Core Requirements -->
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![FFmpeg Required](https://img.shields.io/badge/FFmpeg-required-red)](https://ffmpeg.org/)
[![Manim Version](https://img.shields.io/badge/manim-v0.19.0-orange)](https://www.manim.community/)
[![GitHub Stars](https://img.shields.io/github/stars/HarleyCoops/Math-To-Manim?style=social)](https://github.com/HarleyCoops/Math-To-Manim)

<!-- AI Models / LLMs -->
[![Claude Sonnet 4.5](https://img.shields.io/badge/Claude-Sonnet%204.5-blueviolet)](https://www.anthropic.com)
[![Gemini 3](https://img.shields.io/badge/Gemini-3-4285F4?logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![Kimi K2](https://img.shields.io/badge/Kimi-K2-00D4AA)](https://kimi.moonshot.cn/)
[![DeepSeek R1](https://img.shields.io/badge/DeepSeek-R1-536DFE)](https://www.deepseek.com/)
[![Grok 3](https://img.shields.io/badge/Grok-3-000000)](https://x.ai/)

</div>

[![Star History Chart](https://api.star-history.com/svg?repos=HarleyCoops/Math-To-Manim&type=date&legend=top-left)](https://www.star-history.com/#HarleyCoops/Math-To-Manim&type=date&legend=top-left)

## 效果展示

<div align="center">

**布朗运动：从花粉到投资组合**

![Brownian Motion](public/BrownianFinance.gif)

*从罗伯特·布朗的显微镜到爱因斯坦的热方程，最终抵达金融期权定价的 Black-Scholes 模型。*

---

**递归菱形二十十二面体**

![Recursive Rhombicosidodecahedron](public/Rhombicosidodecahedron.gif)

*一个分形的阿基米德立体，每个顶点都会生成另一个完整的菱形二十十二面体。*

---

**Hopf 纤维化**

![Teaching Hopf](public/TeachingHopf.gif)

*S3 纤维的立体投影生成嵌套环面——纯粹拓扑的 3D 呈现。*

---

**Whiskering Exchange**

![Whiskering Exchange](public/WhiskeringExchangeScene.gif)

*可视化高阶范畴理论中 2-cell 复合的交换律。*

</div>



## 三条 AI 流水线，一个目标

Math-To-Manim 提供 **三条不同的 AI 流水线**。请根据你的 API 访问情况与偏好进行选择：

### 流水线对比

| 特性 | Gemini 3（Google ADK） | Claude Sonnet 4.5 | Kimi K2 |
|:--------|:---------------------|:------------------|:--------|
| **框架** | Google Agent Development Kit | Anthropic Agent SDK | OpenAI-compatible API |
| **架构** | 六代理群体（Swarm） | 六代理流水线 | 三阶段增强 |
| **优势** | 复杂拓扑、物理推理 | 可靠代码生成、递归 | Chain-of-thought、结构化工具 |
| **最佳适用** | 高级 3D 数学、Kerr 度规 | 通用场景、生产使用 | LaTeX 说明为主的场景 |
| **搭建复杂度** | 中等 | 简单 | 简单 |

---

## 流水线 1：Google Gemini 3（ADK）

**位置**：`Gemini3/`

Gemini 流水线使用 **Google Agent Development Kit**，采用六代理群体架构。每个代理都是动画生成流程中的特定角色专家。

### 工作原理

![Gemini Pipeline Architecture](https://mermaid.ink/img/Z3JhcGggVEQKICAgIFVzZXJQcm9tcHRbVXNlciBQcm9tcHRdIC0tPiBDQQogICAgCiAgICBDQVsiPGI+MS4gQ29uY2VwdEFuYWx5emVyPC9iPjxici8+RGVjb25zdHJ1Y3RzIHByb21wdCBpbnRvOjxici8+LSBDb3JlIGNvbmNlcHQ8YnIvPi0gVGFyZ2V0IGF1ZGllbmNlPGJyLz4tIERpZmZpY3VsdHkgbGV2ZWw8YnIvPi0gTWF0aGVtYXRpY2FsIGRvbWFpbiJdCiAgICAKICAgIENBIC0tPiBQRQogICAgUEVbIjxiPjIuIFByZXJlcXVpc2l0ZUV4cGxvcmVyPC9iPjxici8+QnVpbGRzIGtub3dsZWRnZSBEQUc6PGJyLz4nV2hhdCBtdXN0IGJlIHVuZGVyc3Rvb2QgQkVGT1JFIFg/Jzxici8+UmVjdXJzaXZlbHkgZGlzY292ZXJzIGRlcGVuZGVuY2llcyJdCiAgICAKICAgIFBFIC0tPiBNRQogICAgTUVbIjxiPjMuIE1hdGhlbWF0aWNhbEVucmljaGVyPC9iPjxici8+QWRkcyB0byBlYWNoIG5vZGU6PGJyLz4tIExhVGVYIGRlZmluaXRpb25zPGJyLz4tIEtleSBlcXVhdGlvbnM8YnIvPi0gVGhlb3JlbXMvcGh5c2ljYWwgbGF3cyJdCiAgICAKICAgIE1FIC0tPiBWRAogICAgVkRbIjxiPjQuIFZpc3VhbERlc2lnbmVyPC9iPjxici8+RGVzaWducyB1c2luZyBNYW5pbSBwcmltaXRpdmVzOjxici8+LSBWaXN1YWwgbWV0YXBob3JzIChzcGhlcmUgPSBwYXJ0aWNsZSk8YnIvPi0gQ2FtZXJhIG1vdmVtZW50czxici8+LSBDb2xvciBwYWxldHRlIChoZXggY29kZXMpPGJyLz4tIFRyYW5zaXRpb25zIl0KICAgIAogICAgVkQgLS0+IE5DCiAgICBOQ1siPGI+NS4gTmFycmF0aXZlQ29tcG9zZXI8L2I+PGJyLz5XZWF2ZXMgMjAwMCsgdG9rZW4gdmVyYm9zZSBwcm9tcHQ6PGJyLz4tIEV4YWN0IExhVGVYIHN0cmluZ3M8YnIvPi0gQW5pbWF0aW9uIHRpbWluZzxici8+LSBTY2VuZS1ieS1zY2VuZSBkZXNjcmlwdGlvbiJdCiAgICAKICAgIE5DIC0tPiBDRwogICAgQ0dbIjxiPjYuIENvZGVHZW5lcmF0b3I8L2I+PGJyLz5Qcm9kdWNlcyBleGVjdXRhYmxlIE1hbmltIGNvZGU6PGJyLz4tIFRocmVlRFNjZW5lIHdpdGggY2FtZXJhIG1vdmVtZW50czxici8+LSBDb3JyZWN0IExhVGVYIHJlbmRlcmluZzxici8+LSBObyBleHRlcm5hbCBhc3NldHMgcmVxdWlyZWQiXQoKICAgIHN0eWxlIENBIGZpbGw6I2UxZjVmZSxzdHJva2U6IzAxNTc5YixzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIFBFIGZpbGw6I2ZmZjljNCxzdHJva2U6I2ZiYzAyZCxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIE1FIGZpbGw6I2UwZjJmMSxzdHJva2U6IzAwNjk1YyxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIFZEIGZpbGw6I2YzZTVmNSxzdHJva2U6Izg4MGU0ZixzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIE5DIGZpbGw6I2ZmZWJlZSxzdHJva2U6I2I3MWMxYyxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIENHIGZpbGw6I2YxZjhlOSxzdHJva2U6IzMzNjkxZSxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQK)

### 快速开始

```bash
# Set API key
echo "GOOGLE_API_KEY=your_key_here" >> .env

# Run the pipeline
python Gemini3/run_pipeline.py "Explain the Hopf Fibration"
```

### 关键文件

- `Gemini3/run_pipeline.py` - 入口
- `Gemini3/src/agents.py` - 代理定义与系统提示
- `Gemini3/src/pipeline.py` - 编排逻辑
- `Gemini3/docs/GOOGLE_ADK_AGENTS.md` - 完整文档

---

## 流水线 2：Claude Sonnet 4.5（Anthropic SDK）

**位置**：`src/`

Claude 流水线使用 **Anthropic Agent SDK**，提供自动上下文管理与内置工具。

### 工作原理

![Claude Pipeline Architecture](https://mermaid.ink/img/Z3JhcGggVEQKICAgIFVzZXJQcm9tcHRbVXNlciBQcm9tcHRdIC0tPiBDQQogICAgCiAgICBDQVsiPGI+MS4gQ29uY2VwdEFuYWx5emVyPC9iPjxici8+UGFyc2VzIHByb21wdCwgaWRlbnRpZmllczo8YnIvPi0gQ29yZSBjb25jZXB0PGJyLz4tIERvbWFpbiAocGh5c2ljcywgbWF0aCwgQ1MpPGJyLz4tIFZpc3VhbGl6YXRpb24gYXBwcm9hY2giXQogICAgCiAgICBDQSAtLT4gUEUKICAgIFBFWyI8Yj4yLiBQcmVyZXF1aXNpdGVFeHBsb3JlcjwvYj48YnIvPlRIRSBLRVkgSU5OT1ZBVElPTjo8YnIvPlJlY3Vyc2l2ZWx5IGFza3MgJ1doYXQgYmVmb3JlIFg/Jzxici8+QnVpbGRzIGNvbXBsZXRlIGtub3dsZWRnZSB0cmVlPGJyLz5JZGVudGlmaWVzIGZvdW5kYXRpb24gY29uY2VwdHMiXQogICAgCiAgICBQRSAtLT4gTUUKICAgIE1FWyI8Yj4zLiBNYXRoZW1hdGljYWxFbnJpY2hlcjwvYj48YnIvPkVuc3VyZXMgbWF0aGVtYXRpY2FsIHJpZ29yOjxici8+LSBMYVRlWCBmb3IgZXZlcnkgZXF1YXRpb248YnIvPi0gQ29uc2lzdGVudCBub3RhdGlvbjxici8+LSBMaW5rcyBmb3JtdWxhcyB0byB2aXN1YWxzIl0KICAgIAogICAgTUUgLS0+IFZECiAgICBWRFsiPGI+NC4gVmlzdWFsRGVzaWduZXI8L2I+PGJyLz5TcGVjaWZpZXMgZXhhY3QgY2luZW1hdG9ncmFwaHk6PGJyLz4tIENhbWVyYSBhbmdsZXMgYW5kIG1vdmVtZW50czxici8+LSBDb2xvciBzY2hlbWVzIHdpdGggbWVhbmluZzxici8+LSBUaW1pbmcgYW5kIHRyYW5zaXRpb25zIl0KICAgIAogICAgVkQgLS0+IE5DCiAgICBOQ1siPGI+NS4gTmFycmF0aXZlQ29tcG9zZXI8L2I+PGJyLz5XYWxrcyB0cmVlIGZyb20gZm91bmRhdGlvbi0+dGFyZ2V0Ojxici8+LSAyMDAwKyB0b2tlbiB2ZXJib3NlIHByb21wdDxici8+LSBOYXJyYXRpdmUgYXJjIHRocm91Z2ggY29uY2VwdHMiXQogICAgCiAgICBOQyAtLT4gQ0cKICAgIENHWyI8Yj42LiBDb2RlR2VuZXJhdG9yPC9iPjxici8VHJhbnNsYXRlcyB0byBNYW5pbTo8YnIvPi0gV29ya2luZyBQeXRob24gc2NlbmVzPGJyLz4tIEhhbmRsZXMgTGFUZVggcmVuZGVyaW5nPGJyLz4tIDNEIGNhbWVyYSBtb3ZlbWVudHMiXQoKICAgIHN0eWxlIENBIGZpbGw6I2UxZjVmZSxzdHJva2U6IzAxNTc5YixzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIFBFIGZpbGw6I2ZmZjljNCxzdHJva2U6I2ZiYzAyZCxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIE1FIGZpbGw6I2UwZjJmMSxzdHJva2U6IzAwNjk1YyxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIFZEIGZpbGw6I2YzZTVmNSxzdHJva2U6Izg4MGU0ZixzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIE5DIGZpbGw6I2ZmZWJlZSxzdHJva2U6I2I3MWMxYyxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQKICAgIHN0eWxlIENHIGZpbGw6I2YxZjhlOSxzdHJva2U6IzMzNjkxZSxzdHJva2Utd2lkdGg6MnB4LGNvbG9yOmJsYWNrLGFsaWduOmxlZnQK)


### 关键文件

- `src/app_claude.py` - Gradio UI 入口
- `src/agents/prerequisite_explorer_claude.py` - Claude SDK 代理
- `docs/ARCHITECTURE.md` - 系统设计细节

---

## 流水线 3：Kimi K2 Thinking Model

**位置**：`KimiK2Thinking/`

Kimi 流水线使用 Moonshot AI 的 **K2 thinking model**，提供 OpenAI-compatible API 与工具调用接口。

### 工作原理

![Kimi Pipeline Architecture](https://mermaid.ink/img/Z3JhcGggVEQKICAgIFVzZXJQcm9tcHRbVXNlciBQcm9tcHRdIC0tPiBLUEUKICAgIAogICAgS1BFWyI8Yj4xLiBLaW1pUHJlcmVxdWlzaXRlRXhwbG9yZXI8L2I+PGJyLz5CdWlsZHMga25vd2xlZGdlIHRyZWU6PGJyLz4tIFRvb2wtY2FsbGluZyBmb3Igc3RydWN0dXJlZCBvdXRwdXQ8YnIvPi0gVGhpbmtpbmcgbW9kZSBzaG93cyByZWFzb25pbmc8YnIvPi0gUmVjdXJzaXZlIGRlcGVuZGVuY3kgZGlzY292ZXJ5Il0KICAgIAogICAgS1BFIC0tPiBNRQogICAgTUVbIjxiPjIuIE1hdGhlbWF0aWNhbEVucmljaG1lbnQ8L2I+PGJyLz5UaHJlZS1zdGFnZSBlbnJpY2htZW50Ojxici8+LSBNYXRoIEVucmljaGVyOiBMYVRlWCBlcXVhdGlvbnMsIGRlZmluaXRpb25zPGJyLz4tIFZpc3VhbCBEZXNpZ25lcjogRGVzY3JpcHRpb25zIChub3QgTWFuaW0gY2xhc3Nlcyk8YnIvPi0gTmFycmF0aXZlIENvbXBvc2VyOiBDb25uZWN0cyBldmVyeXRoaW5nIl0KICAgIAogICAgTUUgLS0+IENHCiAgICBDR1siPGI+My4gQ29kZUdlbmVyYXRpb248L2I+PGJyLz5GaW5hbCBNYW5pbSBjb2RlOjxici8+LSBGb2N1c2VzIG9uIExhVGVYIHJlbmRlcmluZzxici8+LSBMZXRzIE1hbmltIGhhbmRsZSB2aXN1YWxzPGJyLz4tIFRvb2wgYWRhcHRlciBmb3IgdmVyYm9zZSBpbnN0cnVjdGlvbnMiXQoKICAgIHN0eWxlIEtQRSBmaWxsOiNmZmY5YzQsc3Ryb2tlOiNmYmMwMmQsc3Ryb2tlLXdpZHRoOjJweCxjb2xvcjpibGFjayxhbGlnbjpsZWZ0CiAgICBzdHlsZSBNRSBmaWxsOiNlMGYyZjEsc3Ryb2tlOiMwMDY5NWMsc3Ryb2tlLXdpZHRoOjJweCxjb2xvcjpibGFjayxhbGlnbjpsZWZ0CiAgICBzdHlsZSBDRyBmaWxsOiNmMWY4ZTksc3Ryb2tlOiMzMzY5MWUsc3Ryb2tlLXdpZHRoOjJweCxjb2xvcjpibGFjayxhbGlnbjpsZWZ0Cg==)

### 快速开始

```bash
# Set API key
echo "MOONSHOT_API_KEY=your_key_here" >> .env

# Run prerequisite exploration
python KimiK2Thinking/examples/test_kimi_integration.py

# Run full enrichment pipeline
python KimiK2Thinking/examples/run_enrichment_pipeline.py path/to/tree.json
```

### 关键文件

- `KimiK2Thinking/kimi_client.py` - API 客户端
- `KimiK2Thinking/agents/enrichment_chain.py` - 三阶段流水线
- `KimiK2Thinking/README.md` - 完整文档

---



## 安装

```bash
# Clone repository
git clone https://github.com/HarleyCoops/Math-To-Manim
cd Math-To-Manim

# Install dependencies
pip install -r requirements.txt

# Set up your preferred API key
echo "ANTHROPIC_API_KEY=your_key" >> .env    # For Claude
echo "GOOGLE_API_KEY=your_key" >> .env       # For Gemini
echo "MOONSHOT_API_KEY=your_key" >> .env     # For Kimi

# Install FFmpeg (required for video rendering)
# Windows: choco install ffmpeg
# Linux: sudo apt-get install ffmpeg
# macOS: brew install ffmpeg
```

---

## 运行示例动画

我们提供 **55+ 个可运行示例**，按主题组织：

```bash
# Physics - Black Hole Symphony
manim -pql examples/physics/black_hole_symphony.py BlackHoleSymphony

# Mathematics - Hopf Fibration
manim -pql examples/misc/epic_hopf.py HopfFibrationEpic

# Finance - Option Pricing
manim -pql examples/finance/optionskew.py OptionSkewScene

# Computer Science - Neural Networks
manim -pql examples/computer_science/machine_learning/AlexNet.py AlexNetScene
```

**参数**：`-p` 预览，`-q` 质量（`l` 低，`m` 中，`h` 高，`k` 4K）


浏览全部示例：[docs/EXAMPLES.md](docs/EXAMPLES.md)

---

## 仓库结构

```
Math-To-Manim/
|
+-- src/                    # Claude Sonnet 4.5 pipeline
|   +-- agents/             # Agent implementations
|   +-- app_claude.py       # Gradio UI
|
+-- Gemini3/                # Google Gemini 3 pipeline
|   +-- src/                # Agent definitions
|   +-- docs/               # Gemini-specific docs
|   +-- run_pipeline.py     # Entry point
|
+-- KimiK2Thinking/         # Kimi K2 pipeline
|   +-- agents/             # Enrichment chain
|   +-- examples/           # Usage examples
|
+-- examples/               # 55+ working animations
|   +-- physics/            # Quantum, gravity, particles
|   +-- mathematics/        # Geometry, topology, analysis
|   +-- computer_science/   # ML, algorithms
|   +-- cosmology/          # Cosmic evolution
|   +-- finance/            # Option pricing
|
+-- docs/                   # Documentation
+-- tests/                  # Test suite
+-- tools/                  # Utility scripts
```

---

## 为什么富 LaTeX 提示有效

### 模糊提示的问题

```
"Create an animation showing quantum field theory"
```
**结果**：通用、错误或无法运行的代码。

### 解决方案：详细 LaTeX 提示

```
"Begin with Minkowski spacetime showing the metric:

$$ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$$

Each component highlighted in different hues. Introduce the QED Lagrangian:

$$\mathcal{L}_{\text{QED}} = \bar{\psi}(i \gamma^\mu D_\mu - m)\psi - \tfrac{1}{4}F_{\mu\nu}F^{\mu\nu}$$

with Dirac spinor $\psi$ in orange, covariant derivative $D_\mu$ in green..."
```
**结果**：完美动画，含正确的 LaTeX、镜头运动与时序。

**我们的代理会通过遍历知识树自动生成这类详细提示**。

---

## 常见陷阱（以及我们的解决方式）

| 问题 | 传统方法 | 我们的方案 |
|:--------|:--------------------|:-------------|
| **LaTeX 错误** | 碰运气 | 详细提示给出精确公式 |
| **镜头描述模糊** | “展示量子场” | 指定颜色、角度、时序 |
| **缺少前置知识** | 直接跳到高级主题 | 递归发现依赖关系 |
| **符号不一致** | 混用符号 | 数学增强器保持一致性 |

---

## 技术要求

- **Python**：3.10+
- **API Key**：Anthropic、Google 或 Moonshot
- **FFmpeg**：用于视频渲染
- **Manim Community**：v0.19.0
- **RAM**：最低 8GB，推荐 16GB

---

## 贡献

欢迎贡献：

1. **添加示例**：为新主题创建动画
2. **改进代理**：增强前置知识发现
3. **修复 Bug**：报告并修复问题
4. **文档完善**：改进指南

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 获取指南。

---

## 文档

- [Reverse Knowledge Tree](docs/REVERSE_KNOWLEDGE_TREE.md) - 核心创新
- [Architecture](docs/ARCHITECTURE.md) - 系统设计
- [Examples Catalog](docs/EXAMPLES.md) - 全部 55+ 动画
- [Gemini Pipeline](Gemini3/docs/GOOGLE_ADK_AGENTS.md) - Google ADK 细节
- [Kimi Pipeline](KimiK2Thinking/README.md) - Moonshot AI 集成
- [Quick Start Guide](docs/QUICK_START_GUIDE.md) - 快速上手

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 致谢

- **Manim Community** - 卓越的动画框架
- **Anthropic** - Claude Sonnet 4.5 与 Agent SDK
- **Google** - Gemini 3 与 Agent Development Kit
- **Moonshot AI** - Kimi K2 thinking model
- **1400+ Stargazers** - 感谢支持！

---

<div align="center">

**Built with recursive reasoning, not training data.**

**Star this repo if you find it useful!**

</div>
