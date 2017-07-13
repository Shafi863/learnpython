# This script will take arguments as input
from sys import argv

script, first, second, third = argv
Input1 = input("Provide one more input here: ")
#first = input("Provide the first argument :")
#second = input("Provide the second argument : ")
#third = input("Provide the third one here : ")


print "This script is called : ", script
print "Your first variable is : ", first
print "Your second variable is : ", second
print "Your third variable is: ", third
print "%s + '-'+ %s + '-' + %s + '-' + %s + '-' + %s" %(script,first,second,third,Input1)


