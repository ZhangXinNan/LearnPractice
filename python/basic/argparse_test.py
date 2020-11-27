



import argparse

def str2bool(v):
    return v.lower() in ("true", "t", "1")

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--flag', type=str2bool, default=True)
    return parser.parse_args()


print(get_args())
