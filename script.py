import argparse
parser = argparse.ArgumentParser(description='Running Hyper params')
parser.add_argument('--a', type=float, help='a', default='1')
parser.add_argument('--b', type=float, help='b', default='4')
parser.add_argument('--c', type=float, help='c', default='7')
args = parser.parse_args()
score = args.a ** 2 - args.b ** 2 + args.c
print('cnvrg_tag_score:', score)

