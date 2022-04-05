# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

from subprocess import check_output


def character_counter():
  inputPhrase = input('Enter a word or phrase (if you want to quit, write quit): ')
  if inputPhrase != 'quit':
    print(f'What you entered is {len(inputPhrase)} characters long')
    character_counter()
  else:
    '' 
character_counter()