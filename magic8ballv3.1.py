print ("what is your name?")
name = input()

print ("welcome " + str(name) + " I hope you're ready for your fate.")
import random
r = random.randint(1,3)
def getAnswer(r):

    fortune = [
    'your fate is looking grim' ,
     'your fate will be of nuetral concern' ,
      'your fate is looking most beneficial']

    return fortune[r]

def main():

    answer = getAnswer(r)
    return print(answer)

main()
