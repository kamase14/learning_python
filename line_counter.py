# -*- coding utf-8 -*-
import random

linecount = 0

file = open("word.dat","r",encoding="UTF-8")

for line in file :
    linecount += 1

file.close()

print(linecount)
