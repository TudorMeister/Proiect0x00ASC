import sys

key = str(sys.argv[1])
inputFile = str(sys.argv[2])
outputFile = str(sys.argv[3])
contor = 0
with open(inputFile) as fin:
    with open(outputFile, "w") as fout:
        for c in fin.read():
            fout.write((chr(ord(c) ^ ord(key[contor]))))
            contor += 1
            if (contor == len(key)):
                contor = 0

