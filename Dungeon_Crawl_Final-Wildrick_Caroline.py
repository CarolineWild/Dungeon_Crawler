

import random
import sys

# GLOBAL CONSTANTS
COMMANDS = ("inventory", "i", "inv", "walk", "w", "end")
ROOM_TYPES = ("item collect room", "empty room", "riddle encounter room", "shop")
ITEMS = [("WIZARD'S DIARY", "Every page is full. There's some crazy stuff in here"),("10 coins", "Nice, money!"), ("CHEST", "aaand it's empty."),("WIZARD'S HIGHSCHOOL YEARBOOK PHOTO", "...yikes."), ("WIZARD'S MAGIC NOTES", "just magic jargon")]
EMPTY_ROOM_DESCRIPTIONS = ("You're in an empty hallway with graduate degrees and self portraits lining the halls.", 
"You're in a room with nothing but a cushioned chair and some old books in the corner.", 
"You've found yourself in one of the wizard's studies. There's only pictures of himself on his desk.")

COMBAT_COMMANDS = ("fight", "answer riddle", "run", "insult", "use item")

characters = ["Goblin Man", "Magician", "Dramatic Guy in Cloak", "Gary the Buisness Professional, Financial Freedom Advocate"]
riddles = {
    "The more of me there is, the less you see. What am I?": "Darkness", 
    "It has keys, but no locks. It has space, but no room. You can enter, but can't go inside. What is it?": "Keyboard",
    "What is it that no one wants to have, but no one wants to lose either?": "Lawsuit", 
    "The more you take, the more you leave behind. What am I?": "Footsteps"
}

# GLOBAL VARIABLES
command = None
inventory = ["CAKE"]
lives = 3
coins = 10

def meeting_wizard():
    print("It's just a regular ol' day in the same park you walk through every evening. Not many people are around and the sun is setting.")
    print("As you continue down the park trail, someone cries out loudly from a bench a little ways away...")
    print("'OOOOooooOHHH MY LIFE'")
    print("...just keep walking.")
    print("'OOOOOOOHHHHHH HOW WILL I GO ON'")
    print('''Now that you're a bit closer, you can see the person on the bench is a short old man with a pointy hat and cloak. Between dramatic sighs 
he keeps glancing over at you.''')
    
    # Approach or ignore wizard
    while True:
        approach = input("Approach him or keep walking? (y/n): ").lower()
        if approach == "y":
            print("'OHHH- oh. haha, sorry. Did my existential crisis disturb you?'")
            break
        elif approach == "n":
            print("'EXCUSE ME, YOU OVER THERE. DON'T YOU SEE THAT I'M AN OLD MAN IN DISTRESS? GET OVER HERE!'")
            print("Approach with caution...")
            break
        else:
            print("Please enter a valid input: y/n")

   
    print("'It's just that I have infinite knowledge and a sick beard, and yet here I am all alone... OOOoOO WHYYY MY LIFE.'")
    print("'I mean it really can't be me. I'm a whole wizard, people don't know what they're missing. Right? RIGHT?'")
    print("...")
    
    # Ask for input to comfort the wizard
    input("'What do you think? Do you think I'm cool? At my ripe old age?' (type anything): ")

    # Wizard's response
    print("'WHAT?! ARE YOU KIDDING ME!!! THAT IS THE MOST OFFENSIVE THING I HAVE EVER HEARD.'")
    print("'In any universe, in any timeline, NO ONE has uttered something so—SO—'")
    print("'You know what, LOOK WHAT I CAN DO!'")

    print("The wizard stands up, pulls a wand out of thin air, and begins waving it around.")
    print("The park begins to morph, and the open area suddenly becomes a dark small room with stone walls. The wizard is nowhere to be seen.")

    print("Then the wizard's voice echoes through the stone chamber you now stand in...")
    print("'I'LL SHOW YOU! DON'T THINK I'M COOL? YOU THINK YOU'RE SOO SMART? WELL, LET'S SEE HOW COOL YOU ARE TRAPPED IN MY RIDDLE DUNGEON!'")

def dungeon_introduction():
    print("There are several different paths leading out of the room you're in. You'll need to find the wizard to get out of here.")
    print("Here's what you can do:", COMMANDS)

def game_over():
    print('''
       ____                         ___                 
      / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
     | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
     | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
      \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
          
    ''')

def inventory1():
    print("lives:", lives)
    print("coins:", coins)
    print(inventory)

def shop():  
    global coins, lives, inventory  
  
    FORSALE = [
        ("RIDDLE CLUE", "your deepest secret"), 
        ("MAGIC WAND", "literally anything"), 
        ("INVISIBILITY CLOAK", "10 coins"), 
        ("RIDDLE ANSWER", "1 life")
    ]  
  
    print("Here's what we have for sale:\n")  
  
    for item, price in FORSALE:  
        print(item + " for the cost of", price)  
  
    buying = input("\nWhat would you like to buy?: ").upper()  
  
    for item, price in FORSALE:  
        if buying == item:  
            if buying == "RIDDLE CLUE":  
                print("'Here's your " + item + ". That will cost you", price,"'")  
                inventory.append(item)  
                secret = input("'Well, go on then, Whats the secret?'")  
                print("'Hahah nice. I'm telling everyone.'")  
                break  
            elif buying == "MAGIC WAND":  
                print("'Here's your " + item + ". That will cost you", price,"'")  
                if inventory:  
                    while True:  
                        literally_anything = input("'What item do you have to give me?'").upper()  
                        if literally_anything in [i.upper() for i in inventory]:  
                            inventory.remove(literally_anything.upper())  
                            print("'That works.'")
                            inventory.append(item)  
                            break  
                        else:  
                            print("'You don't have that item. Try again.'")  
                else:  
                    print("'You don't have any items to give me.'")  
                break   
            elif buying == "INVISIBILITY CLOAK":  
                if coins >= 10:  
                    print("'Here's your " + item + ". That will cost you", price,"'")  
                    coins -= 10  
                    inventory.append(item)  
                else:  
                    print("'You don't have enough coins to buy this item.'")  
                break  
            elif buying == "RIDDLE ANSWER":  
                if lives > 1:  
                    print("'Really a life? You know you only get 3 of those right? Eh what do I care'.'")  
                    print("'Here's your " + item + ". That will cost you", price,"'")  
                    lives -= 1  
                    inventory.append(item)  
                else:  
                    print("'You don't have enough lives to buy this item.'")  
                break  
    else:  
        print("'I don't have that. Get lost!'\n")  
  
    print("Your current inventory is:", inventory)  
    print("You have", coins, "coins.")  
    print("You have", lives, "lives.")  
    print("Now get out of my shop.\n")

def handle_use_item(riddle_answer):
    
    print(inventory)
    use_item = input("'What have you got for me?'").upper()

    # Check if the item exists in inventory (case-insensitive)
    if use_item in [item.upper() for item in inventory]:
        # Define item responses
        item_responses = {
            "WIZARD'S DIARY": "'You monster. Using a man's diary against him. Shame on you.'",
            "WIZARD'S MAGIC NOTES": "'Yeah, good luck doing anything with that.'",
            "WIZARD'S HIGHSCHOOL YEARBOOK PHOTO": "'THAT WAS PRE-GLOW UP. PUT THAT AWAY.'",
            "CAKE": "'Tempting, but no.'",
            "INVISIBILITY CLOAK": "'I- That doesn't do much good when you put it on right in front of me.'",
            "MAGIC WAND": "'Ok, so you're clearly not a wizard, so I don't know what you're expecting to happen.'",
            "RIDDLE CLUE": "'Want a hint? Well, do you have a clue?'",
            "RIDDLE ANSWER": "'Ok, the answer is {}'".format(riddle_answer)
        }

        # Print the appropriate response for the selected item
        if use_item in item_responses:
            print(item_responses[use_item])
            if use_item == "RIDDLE CLUE" and "RIDDLE CLUE" in inventory:
                print(f"'Here's your hint: The first letter of the answer is {riddle_answer[0]}'")
                inventory.remove("RIDDLE CLUE")
            elif use_item == "RIDDLE ANSWER":
                inventory.remove("RIDDLE ANSWER")
            
       
        else:
            print("'You don't have that.'")
       

def riddle_encounter():
    global inventory, lives, characters
    
    if room == "riddle encounter room":     # checks that you're in the right room
        print("Here's what you can do:", COMBAT_COMMANDS)
        character = random.choice(characters)
        riddle_list = list(riddles.items())

        if character == "Goblin Man":       # goblin character 
            print("'Well, Well, Well, im the", character,"'")  
            print("Since you think you're so smart,")
            print("'Here's my riddle:'")
            riddle_question, riddle_answer = riddle_list[0]
            print(riddle_question)

            while True:
                combat_command = input("Well, what do you want to do?").lower()
                
                if combat_command == "fight":
                    print("You run at the", character, ",but you pass right through. Oh right. Magic.")
                    continue

                elif combat_command == "answer riddle":
                    riddle_guess = input("What's the answer?").lower()
                    if riddle_guess == riddle_answer.lower():   # prints riddle answer (value) 
                        print("'Ughh. You're right it's", riddle_answer,"'")
                        print("'I guess I'll just cease to exist now'")
                        characters.remove(character)       # deletes character from list so you won't encounter the same one more than once
                        break
                    else:
                        print("Hahah no.")
                        continue

                elif combat_command == "use item":
                    handle_use_item(riddle_answer)

                elif combat_command == "run":
                    print("'Hey, where are you going! Ugh, you'll be back.'")
                    print("..phew that was a close one. We'll circle back to that.")
                    break

                elif combat_command == "insult":
                    print("'Wowww. Low blow. Have you no dignity sir? And yes, you do have to answer my riddle.'")
                    continue
        if character == "Magician":       # Magician 
                    print("'I'm the", character, "No one is impressed with my magic..SIGHHHH. But listen to this riddle:'") 
                    riddle_question, riddle_answer = riddle_list[1]
                    print(riddle_question)

                    while True:
                        combat_command = input("Well, what do you want to do?").lower()
                        
                        if combat_command == "fight":
                            print("You run at the", character, ",but you pass right through. Oh right. Magic.")
                            continue

                        elif combat_command == "answer riddle":
                            riddle_guess = input("What's the answer?").lower()
                            if riddle_guess == riddle_answer.lower():   # prints riddle answer (value) 
                                print("'Ughh. You're right it's", riddle_answer,"'")
                                print("'I guess I'll just cease to exist now.'")
                                characters.remove(character)       # deletes character from list so you won't encounter the same one more than once
                                break
                            else:
                                print("'Hahah no.'")
                                continue

                        elif combat_command == "use item":
                            handle_use_item(riddle_answer)

                        elif combat_command == "run":
                            print("'Hey, where are you going! Ugh, you'll be back.'")
                            print("..phew that was a close one. We'll circle back to that.")
                            break

                        elif combat_command == "insult":
                            print("'Wowww. Low blow. Have you no dignity sir? And yes, you do have to answer my riddle.'")
                            continue
        if character == "Dramatic Guy in Cloak":       # Dramatic guy
                    print("'IT'S ME! THE NOT DRAMATIC ONE! i'm the", character,"'")  
                    print("'BUT MY CLOAK IS JUST COMFORTABLE ITS NOT FOR DRAMATIC EFFECT.'")
                    print("'Anyway, here's my riddle:'")
                    riddle_question, riddle_answer = riddle_list[2]
                    print(riddle_question)

                    while True:
                        combat_command = input("Well, what do you want to do?").lower()
                        
                        if combat_command == "fight":
                            print("You run at the", character, ",but you pass right through. Oh right. Magic.")
                            continue

                        elif combat_command == "answer riddle":
                            riddle_guess = input("What's the answer? ").lower()
                            if riddle_guess == riddle_answer.lower():   # prints riddle answer (value) 
                                print("'Ughh. You're right it's", riddle_answer,"'")
                                print("'I guess I'll just cease to exist now.'")
                                characters.remove(character)       # deletes character from list so you won't encounter the same one more than once
                                break
                            else:
                                print("Hahah no.")
                                continue

                        elif combat_command == "use item":
                            handle_use_item(riddle_answer)

                        elif combat_command == "run":
                            print("'Hey, where are you going! Ugh, you'll be back.'")
                            print("..phew that was a close one. We'll circle back to that.")
                            break

                        elif combat_command == "insult":
                            print("'Wowww. Low blow. Have you no dignity sir? And yes, you do have to answer my riddle.'")
                            continue
        if character == "Gary the Buisness Professional, Financial Freedom Advocate":       #Gary
                    print("'Hey there friend, could I perhaps intrest you in a unlimited passive profit?'")
                    print("...")
                    print("'what?? No!! Of course i'm not trying to sell you a pyramid scheme!'")
                    print("'I'm", character,"'")
                    print("'I'm just putting it out there that you could have unlimited money, but I guess you just want to get right to buisness.'")
                    print("'Here's my riddle:'")
                    riddle_question, riddle_answer = riddle_list[3]
                    print(riddle_question)

                    while True:
                        combat_command = input("Well, what do you want to do?").lower()
                        
                        if combat_command == "fight":
                            print("You run at the", character, ",but you pass right through. Oh right. Magic.")
                            continue

                        elif combat_command == "answer riddle":
                            riddle_guess = input("What's the answer?").lower()
                            if riddle_guess == riddle_answer.lower():   # prints riddle answer (value) 
                                print("'Ughh. You're right it's", riddle_answer,"'")
                                print("'I guess I'll just cease to exist now.'")
                                characters.remove(character)       # deletes character from list so you won't encounter the same one more than once
                                break
                            else:
                                print("'Hahah no.'")
                                continue

                        elif combat_command == "use item":
                            handle_use_item(riddle_answer)

                        elif combat_command == "run":
                            print("'Hey, where are you going! Ugh, you'll be back.'")
                            print("..phew that was a close one. We'll circle back to that.")
                            break

                        elif combat_command == "insult":
                            print("'Wowww. Low blow. Have you no dignity sir? And yes, you do have to answer my riddle.'")
                            continue

def final_wizard_battle():
    global lives  # Declare that we are using the global 'lives' variable
    print("After defeating all 4 of the wizard's riddle masters, a door appears in the middle of the room. You've just found the wizard's chambers.")
    print("The wizard whips his head around when you open the door.")
    print("'WHATTT HOW DID YOU- THOSE RIDDLES WERE THE MOST DIFFICULT I COULD COME UP WITH, AND I KNOW LITERALLY EVERYTHING!'")
    print("'Well, fine. I guess I'll forgive your insult and let you go if you can answer my final riddle...'")
    print("'For each wrong guess, you lose a life. AND DON'T YOU DARE LOOK ANYTHING UP!'")

    guesses = 2  # Number of lives for this specific encounter
    wizard_riddle = "I exist in the shadows, I can be typed but never seen, I can be a burden, yet I can't be ignored, I am left behind as you walk your path. What am I?"
    wizard_riddle_answer = "Legacy"

    print(wizard_riddle)

    # Start the guessing loop
    while guesses > 0:
        wizard_riddle_r = input("'Well? I'm waiting... '").title()  # Take user input and capitalize first letter of each word

        if wizard_riddle_r == wizard_riddle_answer:
            print("You're free! Well that was weird, huh? Now get out of here before the wizard has a second existential crisis. Go!")
            sys.exit()
              # Exit the loop if the answer is correct
        else:
            guesses -= 1
            lives -= 1  # Subtract one life from the global lives variable
            
            if guesses > 0:
                print(f"Wrong answer! You have {guesses} lives left in this encounter. Global lives: {lives}")
            else:
                print("Sorry, you've run out of lives in this encounter. The wizard keeps you locked in the chamber!")
                print(f"Global lives remaining: {lives}")

            if lives == 0:
                game_over()  # Call the game over function if global lives are 0
                sys.exit()  # Exit the function if the player loses all lives

def main():
    print('''
Welcome to the ...
            .______      __   _______   _______   __       _______                             
            |   _  \    |  | |       \ |       \ |  |     |   ____|                            
            |  |_)  |   |  | |  .--.  ||  .--.  ||  |     |  |__                               
            |      /    |  | |  |  |  ||  |  |  ||  |     |   __|                              
            |  |\  \----|  | |  '--'  ||  '--'  ||  `----.|  |____                             
            | _| `._____|__| |_______/ |_______/ |_______||_______|                            
____    __    ____  __   ________      ___      .______      _______       _______.
\   \  /  \  /   / |  | |       /     /   \     |   _  \    |       \     /       |
 \   \/    \/   /  |  | `---/  /     /  ^  \    |  |_)  |   |  .--.  |   |   (----`
  \            /   |  |    /  /     /  /_\  \   |      /    |  |  |  |    \   \    
   \    /\    /    |  |   /  /----./  _____  \  |  |\  \----|  '--'  |.----)   |   
    \__/  \__/     |__|  /________/__/     \__\ | _| `._____|_______/ |_______/    
    .______      ___________    ____  _______ .__   __.   _______  _______             
    |   _  \    |   ____\   \  /   / |   ____||  \ |  |  /  _____||   ____|    O       
    |  |_)  |   |  |__   \   \/   /  |  |__   |   \|  | |  |  __  |  |__               
    |      /    |   __|   \      /   |   __|  |  . `  | |  | |_ | |   __|              
    |  |\  \----|  |____   \    /    |  |____ |  |\   | |  |__| | |  |____             
    | _| `._____|_______|   \__/     |_______||__| \__|  \______| |_______|    O
''')
    print("Enter 'play' to start and 'end' to quit")

    while True:
        game_start = input("start? ").lower()
        if game_start == "end":
            print("Aw darn, bye!")
            return
        elif game_start == "play":
            break
        else:
            print("That's not a valid input.")

    print("Great! Let's get your character set up.")
    while True:
        try:
            name = input("What's your name, stranger?").title()
            if not name:
                raise ValueError("Your name cannot be empty!")
            break
        except ValueError as e:
            print(e)

    print("Nice to meet you,", name, "Let's get started.")

    global command, room
    command = None
    room = None
    while command != "end":
        meeting_wizard()
        dungeon_introduction()

        while True:
            command = input("\nWhat would you like to do?").lower()

            if command == "end":
                print("Thanks for playing!")
                return

            if command not in COMMANDS:
                print("Invalid command. Here's what you can do:", COMMANDS)
                continue

            if command in ("inventory", "i", "inv"):
                inventory1()
            
            elif command in ("walk", "w"):
                print("You take a step forward into the dungeon.")
                room = random.choice(ROOM_TYPES)
    
                if room == "item collect room":
                    print("You've entered a room with a singular item in the center of the floor. Weird. Well, guess its yours now. Finders, keepers.")
                    item2, description = random.choice(ITEMS)
                    print("Looks like you found a", item2 + ":", description)
                    if item2 == "WIZARD'S MAGIC NOTES":
                        inventory.append(item2)
                    
                    elif item2 == "WIZARD'S DIARY":
                        inventory.append(item2)
                    elif item2 == "WIZARD'S HIGHSCHOOL YEARBOOK PHOTO":
                        inventory.append(item2)
                    elif item2 == "10 coins":
                        global coins
                        coins += 10

                elif room == "riddle encounter room":
                    print("\nYou've found a riddle master..")
                    riddle_encounter()

                elif room == "empty room":
                    emptyroom1 = random.choice(EMPTY_ROOM_DESCRIPTIONS)
                    print(emptyroom1)
                    print("Welp, nothing good in here, probably should move on.")

                elif room == "shop":
                    print("pssttt...")
                    print("PPPSSSTTT")
                    print("Hey there,", name, "Yes I, the dissembodied voice, know who you are. Welcome to my traveling shop I guess you could say.")
                    shop()

            if not characters:
                final_wizard_battle()

            
main()
