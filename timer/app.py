import argparse
import log

import yaml

main_parser = argparse.ArgumentParser(description="Record time spent on activities")

main_parser.add_argument("mode",
        help="start or stop an activity",
        choices=["start", "end"])

main_parser.add_argument("name",
        help="activity name")

if __name__ == "__main__":
    args = main_parser.parse_args() 
