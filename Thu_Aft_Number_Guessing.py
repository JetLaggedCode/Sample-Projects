import random

r = random.randint(0,100)   #random number, from 0 to 100

tries = 10
succes = False
for i in range(tries):
    print "You have "+str(tries-i)+" guesses remaining."
    input_str = raw_input()
    guess = int(input_str)
    if(guess == r):
        succes = True
        break
    elif (guess>r):
        print "Your guess is too high."
    else:
        print "Your guess is too low."
if succes == True:
    print "Correct!"
else:
    print "Sorry! You are out of guesses. Please try again."
