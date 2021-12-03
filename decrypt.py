import sys

key = str(sys.argv[1])
inputFile = str(sys.argv[2])
outputFile = str(sys.argv[3])

contor = 0
with open(inputFile, "rb") as fin:
    with open(outputFile, "w", encoding = "UTF-8") as fout:
        content = bytearray(fin.read()).decode("UTF-8")
        #fout.write(str(ord("ù")))
        for c in content:
            #fout.write(str(c)+"\n")
            fout.write((chr(ord(c) ^ ord(key[contor]))))
            contor += 1
            if (contor == len(key)):
                contor = 0

