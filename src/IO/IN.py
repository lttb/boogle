import argparse


def put(* args): return input(* args)


def get_args():
    parser = argparse.ArgumentParser('Boogle')

    parser.add_argument(
        '-e',
        '--engine',
        help='enter engine to use',
        default='google.cse'
    )

    return parser.parse_args()


args = get_args()
