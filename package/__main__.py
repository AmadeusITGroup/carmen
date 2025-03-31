from .module import square
from ._version import __version__


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(prog="Squarer of ints")
    parser.add_argument("x", type=int)
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s, version {__version__}",
    )
    args = parser.parse_args()
    print(f"Square of {args.x} is {square(args.x)}")
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
