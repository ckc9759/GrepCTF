enc = b"gsgsGQ@|9gn8tRy>c\"Mk$gk"
for i in range(len(enc)):
    print(chr(i ^ enc[i]), end='')