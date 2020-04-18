#!/usr/bin/env python3

fobj = open("/tmp/String.txt")
s = fobj.read()
new = []
for i in s:
    if i.isdigit():
        new.append(i)
print(''.join(new))
fobj.close()

