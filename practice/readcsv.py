import csv

FILENAME="student.csv"
DATADIR= "../my work/"


FULLPATH = DATADIR + FILENAME

# print (FULLPATH)
with open (FULLPATH, "rt") as fp:
    #for line in fp:
     #   print (line, end="")
    reader = csv.reader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC)
    total = 0
    linenumber = 0 
    for line in reader:
        if linenumber:
            #print (line)
            total += int(line[1])
        
        linenumber += 1
    print (total)

        