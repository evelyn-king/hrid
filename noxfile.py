"""Run tests for ``hrid`` using ``nox``."""

import nox

PYTHON_VERSIONS = ["3.10", "3.11", "3.12"]


@nox.session(python=PYTHON_VERSIONS)
def test_pip(session):
    """Run tests with all packages installed using pip."""
    session.install(".[all]")
    session.run("pytest")


@nox.session(python=PYTHON_VERSIONS, venv_backend="micromamba")
def test_micromamba(session):
    """Run tests with all packages installed using micromamba."""
    session.install(".[all]")
    session.run("pytest")
