x=1
while x <= 2000:
    def odd_even(x):
        if x%2==0:
            return ". This is an even number."
        else:
            return ". This is an odd number."
    print "Number is " + str(x) + odd_even(x)
    x += 1
