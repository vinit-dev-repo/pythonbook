# cli_demo/count.py
import argparse
from labels import make_label

def main():
    parser = argparse.ArgumentParser(description="Repeat the label GO.")
    parser.add_argument("count", type=int, help="positive repetition count")
    args = parser.parse_args()
    if args.count < 1:
        parser.error("count must be positive")
    print(make_label("go", args.count))

if __name__ == "__main__":
    main()
