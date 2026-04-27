#!/usr/bin/env python3
"""
Generate agent configurations from skills definitions.

This script reads skill definitions and generates corresponding agent
configurations for the marketplace and plugin manifests.
"""

import json
import os
import sys
from pathlib import Path
from typing import Any

# Root directory of the repository
ROOT_DIR = Path(__file__).parent.parent
SKILLS_DIR = ROOT_DIR / "skills"
OUTPUT_DIR = ROOT_DIR / "agents"


def load_skill(skill_path: Path) -> dict[str, Any]:
    """Load a skill definition from a JSON file."""
    with open(skill_path, "r", encoding="utf-8") as f:
        return json.load(f)


def skill_to_agent(skill: dict[str, Any]) -> dict[str, Any]:
    """
    Convert a skill definition to an agent configuration.

    Args:
        skill: The skill definition dictionary.

    Returns:
        An agent configuration dictionary.
    """
    return {
        "id": skill.get("id", ""),
        "name": skill.get("name", ""),
        "description": skill.get("description", ""),
        "version": skill.get("version", "0.1.0"),
        "author": skill.get("author", "unknown"),
        "tags": skill.get("tags", []),
        "capabilities": skill.get("capabilities", []),
        "config": {
            "model": skill.get("model", "gpt-4"),
            "temperature": skill.get("temperature", 0.7),
            "system_prompt": skill.get("system_prompt", ""),
        },
        "metadata": {
            "created_at": skill.get("created_at", ""),
            "updated_at": skill.get("updated_at", ""),
            "license": skill.get("license", "MIT"),
        },
    }


def generate_agents(skills_dir: Path, output_dir: Path) -> list[dict[str, Any]]:
    """
    Generate agent configurations from all skills in the given directory.

    Args:
        skills_dir: Directory containing skill JSON definitions.
        output_dir: Directory to write generated agent configs.

    Returns:
        List of generated agent configurations.
    """
    if not skills_dir.exists():
        print(f"Skills directory not found: {skills_dir}", file=sys.stderr)
        return []

    output_dir.mkdir(parents=True, exist_ok=True)
    agents = []

    for skill_file in sorted(skills_dir.glob("*.json")):
        try:
            skill = load_skill(skill_file)
            agent = skill_to_agent(skill)
            agents.append(agent)

            # Write individual agent file
            agent_file = output_dir / skill_file.name
            with open(agent_file, "w", encoding="utf-8") as f:
                json.dump(agent, f, indent=2, ensure_ascii=False)
                f.write("\n")

            print(f"Generated agent: {agent_file.name}")

        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error processing {skill_file.name}: {e}", file=sys.stderr)

    # Write combined agents index
    index_file = output_dir / "index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump({"agents": agents, "count": len(agents)}, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"\nGenerated {len(agents)} agents -> {output_dir}")
    return agents


def main() -> int:
    """Entry point for the generate-agents script."""
    import argparse

    parser = argparse.ArgumentParser(description="Generate agent configs from skill definitions")
    parser.add_argument(
        "--skills-dir",
        type=Path,
        default=SKILLS_DIR,
        help="Directory containing skill JSON files (default: ./skills)",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=OUTPUT_DIR,
        help="Output directory for generated agents (default: ./agents)",
    )
    args = parser.parse_args()

    agents = generate_agents(args.skills_dir, args.output_dir)
    return 0 if agents is not None else 1


if __name__ == "__main__":
    sys.exit(main())
