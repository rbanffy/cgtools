#!/usr/bin/env python3
import sys

if len(sys.argv) != 4:
    sys.exit("Usage: {} chargen.rom height width".format(sys.argv[1]))

size_v = int(sys.argv[2])
size_h = int(sys.argv[3])

bytes_h = size_h // 8

with open(sys.argv[1], "rb") as f:
    offset = 0
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
                ("{:08b}" * bytes_h)
                .format(*c)
                .replace("0", ".")
                .replace("1", "\u2588"),
            )
        else:
            break
        offset += len(c)
        lines += 1
