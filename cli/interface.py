import argparse

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("-t", "--target", required=True)
    parser.add_argument(
        "-m",
        "--mode",
        choices=["fast", "balenced", "full" "oscp"],
        default="balanced"
    )

    return parser.parse_args()