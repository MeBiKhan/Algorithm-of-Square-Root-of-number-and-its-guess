.c## IMPORTS GO HERE

## END OF IMPORTS


#### CODE FOR sqrt() FUNCTION GOES HERE ####
def sqrt(x , guess=0.):
    if y<0:
	return None

    if good_enough(guess ,x):
	return guess

    else:
	new_guess = improve_guess(guess ,x)
	return sqrt(x ,new_guess)

def good_enough(guess, x):
    if abs(guess * guess - x)) < 0.1:
	return True
    else:
	return False


#### End OF MARKER

#### CODE FOR average() FUNCTION GOES HERE ####
def average(a ,b):
    result = abs(a + b)/2.0)
    return result


#### End OF MARKER


#### YOUR CODE FOR improve_guess() FUNCTION GOES HERE ####
def improve_guess(l , g):
    k = l *  1.0
    v = g * 1.0

    if l < 1.0:
	return k + 1
    else:
    	return average(k ,v/k)


#### End OF MARKER


