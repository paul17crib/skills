# Skills

A fork of [huggingface/skills](https://huggingface.co/skills) — a collection of AI skills, agents, and evaluations.

## Overview

This repository contains:
- **Skills**: Modular AI capabilities that can be composed into agents
- **Agents**: Autonomous AI systems built from skills
- **Evals**: Benchmarks and leaderboards for measuring skill performance
- **Marketplace**: Discoverable plugins for Claude and Cursor

## Structure

```
.
├── .claude-plugin/          # Claude AI plugin configuration
│   ├── plugin.json          # Plugin metadata and entry points
│   └── marketplace.json     # Marketplace listing
├── .cursor-plugin/          # Cursor IDE plugin configuration
│   ├── plugin.json          # Plugin metadata
│   └── marketplace.json     # Marketplace listing
├── .github/
│   └── workflows/
│       ├── generate-agents.yml          # CI: auto-generate agent configs
│       ├── push-evals-leaderboard.yml   # CI: update evals leaderboard
│       └── push-hackers-leaderboard.yml # CI: update hackers leaderboard
└── skills/                  # Core skill implementations
```

## Getting Started

### Prerequisites

- Python 3.10+
- `pip` or `uv` for package management

### Installation

```bash
git clone https://github.com/your-org/skills.git
cd skills
pip install -e .
```

### Running Evaluations

```bash
python -m skills.evals run --skill <skill-name>
```

### Using the Claude Plugin

Install via the Claude marketplace or load the `.claude-plugin/plugin.json` directly in your Claude environment.

### Using the Cursor Plugin

Install via the Cursor marketplace or load the `.cursor-plugin/plugin.json` directly in your Cursor IDE.

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feat/my-skill`)
3. Add your skill under `skills/`
4. Add corresponding evals under `evals/`
5. Open a pull request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

## Security

See [.github/workflows/SECURITY.md](.github/workflows/SECURITY.md) for our security policy.

## License

Apache 2.0 — see [LICENSE](LICENSE) for details.

---

> **Personal fork notes:** I'm using this repo to experiment with building custom skills for my own workflows. Main areas of interest: text summarization and code review skills. Not intended for production use.
>
> **TODO:**
> - [ ] Build a summarization skill that handles long documents (>10k tokens) by chunking
> - [ ] Experiment with a code review skill focused on Python style/type hints
> - [ ] Compare eval results against upstream once I have a baseline
