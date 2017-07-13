def cheese_and_crackers(chesse_count,boxes_of_crackers):
    print "you have %d cheeses!"%chesse_count
    print "you have %d boxes of crackers!" %chesse_count
    print "done.\n"

print "We can just give the function number directly:"
cheese_and_crackers(20,30)
print"Or we can can use variables"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "Or we can do these as well"
cheese_and_crackers(10+50,50-20)

