import argparse
import logging as tracing
import csv
import itertools

# command line arguments
parser = argparse.ArgumentParser(
    prog="Permutation.py",
    description="Parses a given CSV file (by stdin) and outputs all possible permutations of the set.",
    epilog="Please use the justfile (`just run`) to run this script.",
)

parser.add_argument(
    "filename",
    help="The CSV file to parse. If invalid, the script won't run.",
)

parser.add_argument(
    "output",
    help="The CSV file to output into. If invalid, the script won't run.",
)

parser.add_argument(
    "--debug",
    "-d",
    help="Whether or not to emit debug logging information.",
    required=False,
    action="store_true",
)


def permutations(number_list: list[str]) -> itertools.permutations:
    return itertools.permutations(number_list)


def main():
    # parse args
    args = parser.parse_args()

    # setup logging 🤤
    log_level = tracing.DEBUG if args.debug else tracing.INFO
    tracing.basicConfig(
        encoding="utf-8",
        level=log_level,
        format="[%(filename)s:%(lineno)s - %(funcName)s()] %(message)s",
    )

    csv_file = open(args.filename, "r")
    number_list_list: list[list[str]] = list(csv.reader(csv_file, delimiter=","))
    csv_file.close()

    # no idea why it's csv format. it's a comma separated list on ONE LINE. that's .txt's domain
    number_list: list[str] = number_list_list[0]
    tracing.debug(f"number list: {number_list}")

    tracing.debug("ok. let's do them permutations 🤠")
    print()

    output = ""

    with open(args.output, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        for i, perm in enumerate(permutations(number_list)):
            writer.writerow(perm)

    print(output)


if __name__ == "__main__":
    main()
