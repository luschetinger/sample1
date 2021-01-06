#if statement
num1=45
guess=input("please try to guess the number")

if int(guess) == num1:
    print("congratulations, your guess {0} and {1} are the same ".format(guess,num1))

elif int(guess) > num1 :
    print("oh no {0} is larger than{1}".format(guess,num1))

else :
    print("oh no {0} is smaller than {1}".format(guess,num1))

    
