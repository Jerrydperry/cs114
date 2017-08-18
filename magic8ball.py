print ("what is your name?")
name = input()
print ("welcome " + str(name) + " I hope you're ready for your fate.")
import random
ran = random.randint(1,3)


if ran == 1:
    print ("you will suffer a bad end, " +str(name))
if ran == 2:
    print ("your ending will be nuetral, " +str(name))
if ran == 3:
    print ("fate smiles upon you,good end, " +str(name))
