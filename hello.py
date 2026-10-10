"""Tiny hello CLI."""

import argparse


def greet(name: str) -> str:
    return f"hello, {name}!"


def main() -> int:
    parser = argparse.ArgumentParser(description="Say hello.")
    parser.add_argument("name", nargs="?", default="world", help="who to greet")
    args = parser.parse_args()
    print(greet(args.name))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
