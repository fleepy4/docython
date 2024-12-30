from .analyzer.InputChecker import InputChecker
import argparse


def main():
    parser = argparse.ArgumentParser(description="Generate documentation from python file(s)")
    parser.add_argument("-f", "--file", help="for single python file. Use --cfg if you need more", default='')
    parser.add_argument("--cfg", help="path to config file", default='')
    parser.add_argument("-o", "--output", default="docs.html", help="output HTML file name")
    args = parser.parse_args()
    print(args)
    checker = InputChecker(args)
    checker.check_input_completeness()


if __name__ == "__main__":
    main()
