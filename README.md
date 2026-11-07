# ai-pr-lab

一个**刻意做小**的 Python 仓库，用来练完整的 GitHub 协作流程：

```
写代码 → 建分支 → commit → push → 开 PR → CI 跑检查 → AI 评审 → 改代码 → 合并
```

代码本身只有一个统计工具模块，重点是流程，不是业务。

## 里面有什么

| 路径 | 作用 |
| --- | --- |
| `src/calc/stats.py` | 被测代码（mean / median / clamp） |
| `tests/test_stats.py` | pytest 测试 |
| `.github/workflows/ci.yml` | CI：ruff 静态检查 + 3.9/3.11/3.12 三版本跑测试 |
| `.github/workflows/ai-review.yml` | 用 opencode Go 的模型自动评审 PR 并贴评论 |
| `.github/scripts/ai_review.py` | AI 评审脚本，只用标准库 |
| `.github/PULL_REQUEST_TEMPLATE.md` | 开 PR 时自动带出的模板 |
| `docs/练习手册.md` | **从 0 到合并的完整步骤，先看这个** |

## 本地跑起来

需要 `uv`（<https://docs.astral.sh/uv/>），Python 版本由 uv 自动管理。

```powershell
cd E:\code\project\study\ai-pr-lab
uv sync
uv run pytest
uv run ruff check .
```

两条命令都绿，就可以开始按 [`docs/练习手册.md`](docs/练习手册.md) 走了。

## 两种 AI 评审方式

1. **GitHub Copilot code review**（零配置）
   PR 页面 → Reviewers → 选 `Copilot`。需要 Copilot 订阅。

2. **仓库自带的 Action**（用你自己的模型额度）
   在仓库 `Settings → Secrets and variables → Actions` 添加 `OPENCODE_API_KEY`（`oc_sk_...`），
   之后每次开 PR / 推新 commit 都会自动评论。没配 key 时该 job 直接跳过，不会报错。

## 建议的练习顺序

1. 第一次 PR：只改 README 一句话，熟悉 PR 和 CI
2. 第二次 PR：新增 `stdev()`，先故意写错让 CI 变红，再修绿
3. 第三次 PR：加 `percentile()`，让 AI 评审挑出边界条件问题
4. 开分支保护，要求 CI 必须通过才能合并

每一步的具体命令和代码见 `docs/练习手册.md`。
