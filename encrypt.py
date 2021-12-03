import sys

key = str(sys.argv[1])
inputFile = str(sys.argv[2])
outputFile = str(sys.argv[3])
contor = 0
with open(inputFile, encoding = "UTF-8") as fin:
    with open(outputFile, "bw") as fout:
        for c in fin.read():
            c = str(chr(ord(c) ^ ord(key[contor])))
            cnou = bytes(c, "UTF-8")
            fout.write(cnou)
            contor += 1
            if (contor == len(key)):
                contor = 0

