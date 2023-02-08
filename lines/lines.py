import sys
import os

lines = 0

if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):
    if os.path.isfile(sys.argv[1]):
        file = sys.argv[1]
        with open(file, "r") as file:
            for line in file:
                line = line.strip()
                if line.startswith("#") or line == "":
                    continue
                lines += 1

else:
    sys.exit("Invalid")

print(lines)