FILENAME="numbers.txt"
DATADIR= ". .\\my work 2\\"
FILEPATH = "FILENAME + DATADIR"

with open(FILEPATH, "rt") as fP:
    for line in fP:
        print(line)