print ("what is your name?")
name = input()

print ("welcome " + str(name) + " I hope you're ready for your fate.")
import random
r = random.randint(1,3)
def getAnswer(r):
    #  if r == 1:
        #  fortune ='your fate is looking grim.'
    #  elif r == 2:
    #     fortune = 'your fate will be of nuetral concern.'
    #  elif r == 3:
    #     fortune = 'your fate is looking most beneficial'

    fortune = [
    'your fate is looking grim' ,
     'your fate will be of nuetral concern' ,
      'your fate is looking most beneficial']

    if r == 1:
        answer = fortune[1]
    elif r == 2:
        answer = fortune[2]
    elif  r == 3:
        amswer = fortune[3]
    return answer
def main():

    answer = getAnswer(r)
    return print(answer)

main()
