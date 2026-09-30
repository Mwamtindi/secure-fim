import argparse
import json

from securefim.baseline import create_baseline
from securefim.monitor import scan_directory
from securefim.reporter import setup_logger, log_changes, generate_report



def create_parser():
    parser = argparse.ArgumentParser(
        description="SecureFIM - File Integrity Monitoring Tool"
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    baseline_parser = subparsers.add_parser(
        "baseline",
        help="Create a file integrity baseline"
    )
    baseline_parser.add_argument(
        "--directory",
        required=True,
        help="Directory to monitor"
    )
    baseline_parser.add_argument(
        "--output",
        default="baseline.json",
        help="Baseline output file (default: baseline.json)"
    )

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a directory against the baseline"
    )
    scan_parser.add_argument(
        "--directory",
        required=True,
        help="Directory to scan"
    )
    scan_parser.add_argument(
        "--baseline",
        default="baseline.json",
        help="Baseline file (default: baseline.json)"
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    if args.command == "baseline":
        baseline = create_baseline(
            args.directory,
            args.output
        )

        print(f"[+] Baseline created for {len(baseline)} files.")
        print(f"[+] Saved to: {args.output}")

    elif args.command == "scan":
        try:
            with open(args.baseline, "r", encoding="utf-8") as file:
                baseline = json.load(file)
        except FileNotFoundError:
            print(f"[!] Baseline file not found: {args.baseline}")
            return

        results = scan_directory(args.directory, baseline)

        logger = setup_logger()
        log_changes(logger, results)

        generate_report(
        results,
        args.directory
        )

        print("\n=== SecureFIM Scan Results ===")

        print(f"\n[MODIFIED] {len(results['modified'])}")
        for file_path in results["modified"]:
            print(f"  - {file_path}")

        print(f"\n[NEW] {len(results['new'])}")
        for file_path in results["new"]:
            print(f"  - {file_path}")

        print(f"\n[DELETED] {len(results['deleted'])}")
        for file_path in results["deleted"]:
            print(f"  - {file_path}")

        print(f"[+] Report saved to: report.json")


if __name__ == "__main__":
    main()