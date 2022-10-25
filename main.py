import random 

num = random.randrange(1,20)

stop = 0
while stop == 0:
  guess = int(input("Guess the random number "))
  if guess < num:
    print ("Your guess is too low ")
  elif guess > num:
    print ("Your guess is too high ")
  elif guess >= num:
    print ("Bingo!")
