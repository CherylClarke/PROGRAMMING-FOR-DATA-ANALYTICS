# program that reads a file and takes action
# Author : Andrew Beatty

FILENAME="numbers.txt"
# IF FILE IS IN DIFFERENT DIRECTORY, SET PATH HERE
DATADIR= "../../my work/"

FULLPATH = DATADIR + FILENAME

# print (FULLPATH)

with open (FULLPATH, "rt") as fp:
    for line in fp:
        print (line)