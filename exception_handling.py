
x = -1

try:
    print(x)
except NameError:
    print("Sorry, variable x is not defined.")
else:
    print("Everything went fine")
    
if x < 0:
    raise Exception("Sorry, no numbers below zero")       
    
    