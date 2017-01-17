# -*- coding utf-8 -*-
import random

tmp_list = list()
word_list = list()

file = open("word.dat","r",encoding="UTF-8")

for line in file :
    tmp_list = line.split(" ")
    word_list.append(tmp_list[1])

file.close()

print(word_list[random.randint(0,9)])

