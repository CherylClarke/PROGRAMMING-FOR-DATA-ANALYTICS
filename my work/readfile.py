FILENAME="numbers.txt"
DATADIR="..\\my work 2\\"
FILEPATH = "DATADIR + FILENAME"

with open(FILEPATH, "rt") as fP:
    for line in fP:
        print(line)