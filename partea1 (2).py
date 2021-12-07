with open("input.txt") as fin:
    s = fin.read()
    with open("output", "rb") as fout:
        t = bytearray(fout.read())
        i = 0
        for c in t:
            print(chr(ord(chr(c)) ^ ord(s[i])), end = "")
            i += 1
            if i == 14:
                break






