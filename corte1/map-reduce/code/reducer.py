import sys

curkey = None
total = 0

for line in sys.stdin:
        key, val = line.split("\t")
        val = int(val)

        if key == curkey:
                total += val
        else:

                if curkey is not None:
                        print(curkey, "\t", total)
                curkey = key
                total = val

print(curkey, "\t", total)