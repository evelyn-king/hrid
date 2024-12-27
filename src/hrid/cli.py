"""CLI for hrid."""

import argparse

from hrid import hrid


def main():
    """Define the parser for the ``hrid`` CLI."""
    parser = argparse.ArgumentParser(prog="hrid", description="Generate a human readable id.")
    parser.add_argument("--seed", default=None)
    args = parser.parse_args()
    generated_id = hrid(seed=args.seed)
    print(generated_id)


if __name__ == "__main__":
    main()
