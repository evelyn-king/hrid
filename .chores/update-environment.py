"""Update environment.yml from pyproject.toml."""

from __future__ import annotations

import tomllib


def generate_environment_yml(
    data: dict,
    sections: tuple[str, ...] = ("test", "docs"),
    default_packages: tuple[str, ...] = ("python",),
) -> str:
    """Generate environment.yaml from pyproject.toml."""
    env_yaml = "# This file is generated from pyproject.toml using .chores/update-environment.py\n"
    env_yaml += "name: hrid\n\n"
    env_yaml += "channels:\n- conda-forge\n\n"
    env_yaml += "dependencies:\n"

    # Default packages
    for package in default_packages:
        env_yaml += f"  - {package}\n"

    # Required deps from pyproject.toml
    env_yaml += "  # from pyproject.toml\n"
    for dep in data["project"]["dependencies"]:
        env_yaml += f"  - {dep}\n"

    # Optional dependencies
    for group in data["project"]["optional-dependencies"]:
        if group not in sections:
            continue
        env_yaml += f"  # optional-dependencies: {group}\n"
        for dep in data["project"]["optional-dependencies"][group]:
            env_yaml += f"  - {dep}\n"

    return env_yaml


if __name__ == "__main__":
    # Load pyproject.toml
    with open("pyproject.toml", encoding="utf-8") as f:  # noqa: PTH123
        data = tomllib.loads(f.read())

    # Generate environment.yml
    environment_yml = generate_environment_yml(data, sections=("test",))

    # Save environment.yml
    with open("environment.yaml", "w", encoding="utf-8") as f:  # noqa: PTH123
        f.write(environment_yml)

    # Generate environment.yml
    environment_yml = generate_environment_yml(data, sections=("test", "docs"))

    # Save environment.yml
    with open("docs/environment.yaml", "w", encoding="utf-8") as f:  # noqa: PTH123
        f.write(environment_yml)
