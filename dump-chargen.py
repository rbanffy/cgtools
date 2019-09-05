#!/usr/bin/env python3
import sys

if len(sys.argv) != 5:
    sys.exit("Usage: {} chargen.rom height width offset".format(sys.argv[0]))

size_v = int(sys.argv[2])
size_h = int(sys.argv[3])

bytes_h = size_h // 8

offset = int(sys.argv[4])

with open(sys.argv[1], "rb") as f:
    f.seek(offset)
    lines = 0
    symbol = 0
    while True:
        c = f.read(bytes_h)
        if c:
            if (lines % size_v) == 0:
                print("\n {0:4d}".format(symbol))
                symbol += 1
            print(
                "{0:7n}".format(offset),
                ("{:08b}" * len(c))
                .format(*c)
                .replace("0", ".")
                .replace("1", "\u2588"),
            )
        else:
            break
        offset += len(c)
        lines += 1
