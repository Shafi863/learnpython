# this script will open a file
from sys import argv
#these are arguments
script,filename = argv
#Here we open the file
#prompt = "> "
#filename = raw_input(prompt)
txt = open(filename)

#Here we print the contents of the file
print "Here's your file %r:" %filename
print txt.read()
open(filename)
#print txt.readline(100)
txt.write("This is to be appended")
#txt.close()
