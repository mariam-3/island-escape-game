# Variables
player_name = ''

difficulty_message = '''
The first choice you will need to choose your difficulty level
Please enter the number next to your chosen difficulty
(1) Easy (3 lives)
(2) Normal (2 lives)
(3) Hard (1 life) 
'''

game_rules = '''
It’s now almost time to finally get playing!
First though, follow these guidelines to make sure this games goes smoothly
1. If your options are in a numbered list, answer the question with a number.
2. If, on the other hand, the question doesn’t give options, answer with yes/no.
3. The case of your answers doesn’t matter.
4. Remember to take risks!
'''

bad_ending_message = '''
As the sun sets, you gently place the final piece of wood.
You may be safe now, but you are still itching to know 
what mysteries this island holds...'''

# The list of stages, each stage is a dictionary:
stages = [{
    'intro': '''
   It’s 1653. The last thing you remember is encountering pirates while swimming. 
   You don’t know where you are, but you can still hear water crashing nearby.
   Wait a minute. This must mean you’re outside. Why can’t you see anything? 
   Putting your hands to your face, you realise your eyes are covered with a blindfold, 
   and it seems to be made of paper...
   ''',
    'question': '''Do you jump into the water to take it off?''',
    'choices': ['yes', 'no'],
    'correct': 'yes',
    'success': 'Success! Your blindfold came off!',
    'fail': f'{player_name} starved to death!',
    'bad_ending': False,
}, {
    'intro':
    '''As you approach shore, you realise something is.. off about your hometown.
   You brush this aside  
   As you clamber onto a rock to catch your breath, it hits you.
   This island lacks the shaky timber shacks that normally extend along the shore.''',
    'question': '''Do you, 
     1) look for your hometown or 
     2) set up camp before dark sets in? ''',
    'choices': ['1', '2'],
    'correct': '2',
    'success': '',
    'fail': f'{player_name} was attacked by a black bear.',
    'bad_ending': False,
}, {
    'intro': '''Looking around, you notice that there are logs 
       stretching into the distance as far as the eye can see. 
       This island can't be uninhabited...''',
    'question': '''Do you
       1) Use the wood around you to build shelter or
       2) Look for the inhabitants?''',
    'choices': ['1', '2'],
    'correct': '2',
    'success': '',
    'fail': '',
    'bad_ending': True,
}, {
    'intro': '''Just when you were about to give up and return to your shelter,
     you catch a glimpse of faint light in the distance.''',
    'question': '''Do you
     1) investigate closer
     2) go home?''',
    'choices': ['1', '2'],
    'correct': '1',
    'success': '',
    'fail': '',
    'bad _ending': True,
}, {
    'intro':
    '''As you trek to the edge of the cliff, you spot the source of the 
light:
a village!
However, There is one problem; you need to climb down from the top of the mountain to 
get there, and it seems like a dangerous trip.''',
    'question': '''Do you
      1) Take the risk or
      2) Turn around and go home?''',
    'choices': ['1', '2'],
    'correct': '1',
    'success':
    "With the villagers' help, you sail home and live happily ever after",
    'fail': '',
    'bad_ending': True,
}]

# Defining the class Player
class Player:

  # Initializing method
  def __init__(self, player_name, lives):
    self.player_name = player_name
    self.lives = lives

  # A method to test if the player has enough lives to continue
  def is_alive(self):
    return self.lives > 0

  # A method to substract a life 
  # and end the game if they have no lives
  def get_hit(self):
    if self.is_alive():
      self.lives -= 1
      print(f'You lost a life. Remaining lives: {self.lives}')
    if not self.is_alive():
      print('You lost all of your lives. Game over!')
      exit()


# Start from here

# Get the player name and assign it to a variable
player_name = input("Hi there! what's your name? ")

print(f'Welcome {player_name}!')

difficulty = input(difficulty_message)

# Check the difficulty input validity
while (difficulty != '1' and difficulty != '2' and difficulty != '3'): 
  difficulty = input('Please choose a valid number from the list above: ')

# Set the number of lives based on the chosen difficulty
if difficulty == '1': 
  lives = 3
  print('your difficulty: easy')
elif difficulty == '2':
  lives = 2
  print('your difficulty: normal')
else:
  lives = 1
  print('your difficulty: hard')

# Create a player object using "Player" class
player = Player(player_name, lives)

print(game_rules)

# Go through all stages
for stage in stages:
  
  # The player can play only if they have enough lives
  while player.is_alive():
    print('-----------------------------------')
    print(stage['intro'])

    # Get the user's answer and make it in lower case
    # so we can compare it and cover all compinations of cases
    answer = input(stage['question']).lower()

    # Check the answer validity,
    # as it should be one of the stage choices
    while answer not in stage['choices']:
      print('Invalid choice!')
      answer = input(stage['question']).lower()

    # If the answer is correct
    if answer == stage['correct']:
      print(stage['success'])
      # then, go to the next stage
      break

    # If the answer is incorrect
    # and the stage has a bad ending
    elif stage['bad_ending']:
      print(bad_ending_message)
      # then, end the game
      exit()

    # If the answer is incorrect
    # and the stage has no bad ending
    else:
      print(stage['fail'])
      # then, the player loses a life
      # and restart the stage,
      # if they have enough lives remaining
      player.get_hit()

# End the game
exit()
