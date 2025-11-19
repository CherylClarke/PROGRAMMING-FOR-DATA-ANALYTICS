# program that reads a file and takes action
# Author : Andrew Beatty

FILENAME="number.txt"
# IF FILE IS IN DIFFERENT DIRECTORY, SET PATH HERE
DATADIR= "../my work/"

FULLPATH = DATADIR + FILENAME

# print (FULLPATH)

with open (FULLPATH, "rt") as fp:
    total = 0
    for line in fp:

      #  print (f" {line} has length {len(line)}")

        print (f" {line.strip()} ", end="")
        print ( f"has length {len(line)}")
        total += int(line)
    print (total)
# this will put them ob the same line to avoid last line break (new line characters)
   