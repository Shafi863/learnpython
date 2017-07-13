def add(a,b):
    print " ADDING %d + %d" %(a,b)
    return a+b

def subtract(a,b):
    print "SUBTRACTING %d - %d,"%(a,b)
    return a-b

def multiply(a,b):
    print "MULTIPLYIN %d X %d,"%(a,b)
    return a*b

def divide (a,b):
    print "Dividing %d / %d,"%(a,b)
    return a/b

print "Let's do some math with functions!"

age = add(5,25)
height = subtract(160,5)
weight = multiply(33,2)
iq=divide(240,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" %(age,height,weight,iq)
print ("Here is the puzzle:")

what = add(age,subtract(height,multiply(weight,divide(iq,2))))
when = subtract(age,add(height,divide(weight,multiply(iq,2))))

print "That becomes: ", what
print "This becomes: ",when
