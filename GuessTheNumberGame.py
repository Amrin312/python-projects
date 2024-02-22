import random
print('Guess the number')
print('You have 10 chances to guess the number. Number ranges from 1-50')

numchance = 1
while numchance <=10:
   randnum = random.randrange(1,50)
   getinp = int(input('Enter the number range from 1-50'))
   if(randnum == getinp):
      print('Correct!')
      break
   else:
      print('Try again!')
   numchance+=1
if(numchance>10):
    print("Sorry, you've reached the maximum number of attempts. The correct number was {randnum}.")


