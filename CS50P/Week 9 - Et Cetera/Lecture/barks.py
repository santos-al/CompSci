# import sys

# if len(sys.argv) == 1:
#   print("bark")
# elif len(sys.argv) == 3 and sys.arv[1] == "-n":
#   n = int(sys.argv[2])
#   for _ in range(n):
#     print("bark")
# else:
#   print("usage: barks.py") 

import argparse

parser = argparse.ArgumentParser(description="Bark like a dog")
parser.add_argument("-n", default=1, help="Number of times to bark", type=int)
args = parser.parse_args()

for _ in range(int(args.n)):
  print("barks")