from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s "%(from_file,to_file)

#input = open(from_file)
#indata = input.read()

#indata = open(from_file).read()
output = open(to_file,'w').write(open(from_file).read())
#print "The input file is %d bytes long" %len(indata)

#print "Does the output file really exists? %r" %exists(to_file)
#print "Ready, hit RETURN to continue, CRTL-c to abort."
#raw_input()



print "Alright, all done."

#output.close()
#input.close()