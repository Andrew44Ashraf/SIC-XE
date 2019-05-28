import sys 
import os



f = open('intermediate.txt') 
outfile = open("dataset.txt", "w")
lines = f.readlines()
f.close()

for i, line in enumerate(lines): 
    word= f.readline
    outfile.write(str(word))

f.close() 