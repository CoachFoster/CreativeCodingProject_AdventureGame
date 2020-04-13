#################################
# Create Your Own Adventure Game 
#################################

import time

# set terminal output colors
pcred = "\033[91m"
pcgreen = "\033[92m"
pcyellow = "\033[93m"
pcblue = "\033[94m"
pcend = "\033[0m"

# game text template
# print(pcblue + 'insert_text' + pcend)

# Introduction
print(pcblue + 'Welcome to the North Georgia Mountain Adventure Game!' + pcend)
print(pcblue + '*****************************************************' + pcend)
time.sleep(1)

print(pcblue + 'You are visiting Blue Ridge, Georgia.' + pcend)
print(pcblue + 'You decide to go for an evening hike alone in the mountains.' + pcend)

# choose an item
print(pcblue + 'You can pick one item to take with you - ' + pcend)
print(pcblue + 'map (m), flashlight (f), chocolate (c), rope (r), or stick (s).' + pcend)

item = input('What do you choose?: ')
item = item.lower()
valid_items = ['m', 'f', 'c', 'r', 's']

while item not in valid_items:
  print(pcyellow + 'Invalid input' + pcend)
  item = input('Please enter m for map, f for flashlight, c for chocolate, r for rope, or s for stick: ')

# humming sound - to follow or not to follow?
print(pcblue + 'You hear a humming sound.' + pcend)
choice1 = input('Do you follow the sound? Enter y or n: ')

while choice1.lower() not in ['y', 'n']:
  print(pcyellow + 'Invalid input' + pcend)
  choice1 = input('Please enter y for yes, or n for no: ')

if choice1.lower() == 'y':
  print(pcblue + 'You keep moving closer to the sound.' + pcend)
  print(pcblue + 'The sound suddenly stops.' + pcend)
  time.sleep(4)
  print(pcblue + 'You are now LOST! ... ' + pcend)
  print(pcblue + 'You try to make a call on your phone, but there is no signal!' + pcend)

  # pick a direction
  direction = input('Which direction to you go? Enter north, south, east, or west: ')
  direction = direction.lower()
  valid_directions = ['north', 'south', 'east', 'west']

  while direction not in valid_directions:
    print(pcyellow + 'Invalid input' + pcend)
    direction = input('Please enter north, south, east, or west: ')
    direction = direction.lower()

  if direction == 'north':
    print(pcblue + 'You reach an abandoned cabin.' + pcend)
    time.sleep(2)
    if item == 'm':
      print(pcblue + 'You use the map and find your way home.' + pcend)
      print(pcgreen + 'CONGRATULATIONS! You won the game.' + pcend)
    else:
      print(pcblue + 'If you had a map, you could find your way from here.' + pcend)
      print(pcred + '---You are still lost. You lost the game.---' + pcend)
  elif direction == 'south':
    print(pcblue + 'You reach a river with a broken bridge.' + pcend)
    time.sleep(2)
    if item == 'r' or item == 's':
      print(pcblue + 'Luckily, you chose an item that can fix the bridge.' + pcend)
      print(pcblue + 'You fix the bridge, cross over, and find your way home.' + pcend)
      print(pcgreen + 'CONGRATULATIONS! You won the game.' + pcend)
    else:
      print(pcblue + 'If you had a rope or a stick, you could fix the bridge.' + pcend)
      print(pcred + '---You are still lost. You lost the game.---' + pcend)
  elif direction == 'east':
    print(pcblue + 'You reach the side of the highway. It is dark.' + pcend)
    time.sleep(2)
    if item == 'f':
      print(pcblue + 'You use the flashlight to signal for help.' + pcend)
      print(pcblue + 'A car stops and gives you a ride home.' + pcend)
      print(pcgreen + 'CONGRATULATIONS! You won the game.' + pcend)
    else:
      print(pcblue + 'If you had a flashlight, you could signal for help.' + pcend)
      print(pcred + '---You are still lost. You lost the game.---' + pcend)
  else:
      print(pcblue + 'You are waking and trip over a fallen long.' + pcend)
      print(pcblue + 'You hurt your foot. You sit down to wait for help.' + pcend)
      time.sleep(2)
      print(pcblue + 'This could be a long time.' + pcend)
      time.sleep(4)
      print(pcred + '---You are still lost. You lost the game.---' + pcend)
else:
  print(pcblue + 'Good idea. You are not taking risks.' + pcend)
  print(pcblue + 'You head in the direction of your starting point.' + pcend)
  time.sleep(2)
  print(pcblue + 'You realize that you are LOST!' + pcend)
  time.sleep(2)
  print(pcblue + 'The sound is behind you and it is getting louder. You panic!' + pcend)

  # run or make a call?
  action = input('Do you start running (r), or stop to make a call (c)?: ')

  while action.lower() == 'c':
    print(pcblue + 'The call does not go through.' + pcend)
    action = input('Do you start running (r), or stop to make a call (c)?: ')
  
  print(pcblue + 'You are running fast. The sound gets really loud.' + pcend)
  time.sleep(4)
  print(pcblue + 'A woman on an electric scooter comes up behind you.' + pcend)
  time.sleep(2)

  answer = input('She asks, "What is your favorite computer programming language?": ')
  answer = answer.lower()

  if answer == 'python':
    time.sleep(2)
    print(pcblue + 'She says, "Yes, that is my favorite, too.' + pcend)
    time.sleep(2)
    print(pcblue + '"If you have some chocolate, I will help you."' + pcend)
    
    if item == 'c':
      print(pcblue + 'Luckily, you choose correctly!' + pcend)
      print(pcblue + 'You give the woman the chocolate.' + pcend)
      time.sleep(2)
      print(pcblue + 'She helps you get home.' + pcend)
      print(pcgreen + 'CONGRATULATIONS! You won the game.' + pcend)
    else:
      print(pcblue + 'You should have chosen that chocolate!' + pcend)
      time.sleep(2)
      print(pcblue + 'She rides away, leaving you alone and lost.' + pcend)
      print(pcred + '---You lost the game.---' + pcend)
  else:
    time.sleep(5)
    print(pcblue + 'She did not like your answer.' + pcend)
    print(pcblue + 'She rides away, leaving you alone and lost.' + pcend)
    print(pcred + '---You lost the game.---' + pcend)

# The End