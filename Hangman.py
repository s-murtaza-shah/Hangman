#             Title: Hangman 
# 
#        Programmer: S. Murtaza Shah (99059sha) 
# 
#       Description: This program is an interactive hangman game. The player is
#                    presented with a random phrase/ word which they try to guess
#                    by entering in letters or the phrase in full. As the player
#                    guesses the correct words, the letters start appearing. The
#                    player has to guess it correctly within 6 incorrect tries.
# ______________________________________________________________________________ 

# The following function gets the user to press enter to continue. Also takes in
# one argument which is the user's name to format the user's name in the statement.
def PressEnter(name):
    """Gets the user to press enter to continue and formats their name into the statement""" 
    input("\n{}, please press enter to continue...".format(name))

# The following function adds 25 new lines to clear the screen, and puts
# underscores to divide the screen into a section.
def FormatScreen():
    """Clears and formats the screen by adding new lines and printing underscores so that it is cleared of previous text"""
    print("\n"*25)
    print("_"*80)


    
################    
# MAIN PROGRAM #
################

# Start loop (the whole game is inside it)
while True:

    # Initialize wrong to 6 
    wrong = 6

    # Initialize the numOfLetters (in puzzle) to zero.
    numOfLetters = 0

    # Initialize hidden letters (num of letters in hidden) to zero.
    hiddenLetters = 0

    # Initialize the hidden string (empty)
    hidden = ""

    # Initialize spacedOut (puzzle chars which are spaced out - used in .format())
    # spacedOut is currently empty
    spacedOut = ""

    # Initialize guessedLetters to empty. This will start to have values when the
    # player guesses a letter.
    guessedLetters = ""

    # Initialize the printed string to empty. This is used so that the "success"
    # print statement only gets printed once even if there are multiple of those
    # specific letters.
    printed = ""

    # Initialize the incorrectLetters to empty. Will contain all the incorrect letters
    incorrectLetters = ""

    # Initialize the tries to 1. The amount of tries the user takes.
    tries = 1

    # Initialize the chooseLetter string to all the alphabets.
    chooseLetter = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"

    # ASCII art in an array
    # Displays all the different images of the hangman
    hangman = [""" 

  |-----| \n  |     0 \n  |    /|\ \n  |   / | \ \n  |     | \n  |    / \ \n  |   /   \ \n _|____
               
                                                     """,
            """

  |-----| \n  |     0 \n  |    /|\ \n  |   / | \ \n  |     | \n  |    /  \n  |   /    \n _|____

                                                    """,
           """

  |-----| \n  |     0 \n  |    /|\ \n  |   / | \ \n  |     | \n  |      \n  |       \n _|____
                                                    """,

           """

  |-----| \n  |     0 \n  |    /| \n  |   / |  \n  |     | \n  |      \n  |       \n _|____
                                                    """,

           """

  |-----| \n  |     0 \n  |     | \n  |     |  \n  |     | \n  |      \n  |       \n _|____
                                                    """,
           """
  |-----| \n  |     0 \n  |       \n  |        \n  |       \n  |      \n  |       \n _|____

                                                    """,
           """

  |----| \n  |       \n  |       \n  |        \n  |       \n  |      \n  |       \n _|____

                                                    """]
 
    # Displays title which is centered    
    print("WELCOME TO MURTAZA'S HANGMAN!\n".center(80))

    # Following block of print statements display the introduction and
    # instructions
    print("This is a fun hangman game. You are presented with a random phrase")
    print("if you enter a random number, or you could also make your own phrase")
    print("by entering 0. However, if you want to make your own puzzle, you would")
    print("need 2 players - 1 person makes the puzzle, the other guesses it. As the")
    print("player guesses the correct letters, the letters will start appearing in")
    print("the unknown word/ phrase. The category is the only hint the player gets!")
    print("To begin, please follow the instructions below: ")

    # storing 26 pre-programmed puzzles in an array (myPuzzles)
    # This is so that the user doesn't necessarily need a partner.
    myPuzzles = ["PROGRAMMING IS VERY FUN!", "ALWAYS ACCEPT CHALLENGES!",
                 "WELCOME TO HANGMAN", "ENTHUSIASTIC", "SNOWY, COLD WINTER",
                 "MAKE MISTAKES AND LEARN!","BIRDS SINGING SWEETLY",
                 "SOCCER IS THE BEST!", '"SKY IS THE LIMIT"', '"TIME IS MONEY"',
                 "WILD HORSES RACING!", "TORONTO BLUE JAYS", "EDUCATION",
                 "TECHNOLOGY ROCKS!", "FLOWERS BLOOM IN SPRING",
                 "HAVE FUN WITH FRIENDS!", "CANADA IS A HUGE COUNTRY!",
                 "BEACHES ARE FUN TO VISIT!", "DO EXERCISE AND STAY ACTIVE",
                 "RURAL AREAS ARE PEACEFUL", "NATURE IS BEAUTIFUL!",
                 "JUPITER IS A GIANT PLANET!", "RUNNING A MARATHON",
                 "MATHEMATICS IS COOL!", "OUR PLANET EARTH!", "XYLOPHONE"]

    # storing 26 pre-programmed categories in an array (myCategories)
    # This is so that the user doesn't necessarily need a partner.
    myCategories = ["computers", "inspirational phrase", "game", "adjective",
                    "season", "optimistic quotes", "nature", "physical activity",
                    "inspirational quote", "valuable lesson", "animals", "teams",
                    "nouns", "innovations", "beautiful things", "enjoyment activities",
                    "country", "places", "activities", "areas", "surroundings",
                    "space items", "long-duration physical activities", "subjects",
                    "things we love", "instruments"]

    # Start loop (error trap for what the user wants to do. Play a random
    # pre-programmed puzzle, or play with a partner.
    while True:

        # Ask the user for what they want to do by asking them to enter
        # appropriate numbers
        puzzleNum = int(input("\nEnter a number between 1 - 26 to select a random puzzle (0 to customize): "))

        # Check if the user enters a number between 1-26 or enters a 0. If so,
        # break out of loop
        if puzzleNum >= 0 and puzzleNum <= 26:
            break

        # Otherwise, print an error message
        print("Enter 0 or enter a number between 1 and 26.")

    # Check if the user entered anything but 0 (which would be a number between
    # 1 and 26.
    if puzzleNum != 0:

        # If so, a specific puzzle and a specific category is going to be set
        # depending on what number the user enters. The index to access the
        # puzzles and categories is always 1 less than what the user enters as
        # the indexing starts at 0.
        puzzle = myPuzzles[puzzleNum-1]
        category = myCategories[puzzleNum-1]

    
    # Otherwise (number is 0)    
    else:

        # Make the user aware that if they don't enter a name, their name will
        # be set to "Guest".
        print("\nNOTE: your name will be 'Guest' if you don't enter a name.")

        # Since a puzzle maker is involved, ask their name. Convert their name
        # into a capitalized string if it's not capitalized already.
        makerName = input("Enter your name (puzzle maker): ").title()

        # Check if no name is entered, if so, set the name to "Guest".
        if makerName == "":
            makerName = "Guest"

        # Start error trap for the puzzle
        while True:

            # Ask the puzzle maker (user) for the puzzle. User's name is formatted
            # into the prompt. Convert puzzle to uppercase.
            puzzle = input("\n{}, please enter a puzzle: ".format(makerName)).upper()

            # initialize counter to 0. Used for checking if there are any letters
            # in the puzzle
            letterCounter = 0

            # Start for loop which repeats the amount of chars in the puzzle
            for i in range(len(puzzle)):

                # Check if that one char in puzzle is between A and Z, if so, add
                # one to the letter counter
                if puzzle[i] >= "A" and puzzle[i] <= "Z":
                    letterCounter += 1

            # Check if the length of puzzle is between 2-30 chars (reasonable length)
            # Check if there are at least 2 letters in the puzzle.
            if len(puzzle) >= 2 and len(puzzle) <= 30 and letterCounter >= 2:
                break

            # Otherwise, print an error message
            print("{}, enter a puzzle with 2-30 characters and at least 2 letters.".format(makerName))

        # Start error trap for category
        while True:

            # Ask user for category. Name formatted into the prompt.
            category = input("\n{}, please enter a category: ".format(makerName))

            # Initialize letter counter to zero. Used for checking letters in the
            # category entered by the user.
            letterCounter2 = 0

            # Start for loop which repeats the amount of chars in the puzzle
            for i in range(len(category)):

                # Check if that one char in category is between A and Z, if so, add
                # one to the letter counter
                if category[i] >= "a" and category[i] <= "z" or (category[i] >= "A" and category[i] <= "Z"):
                    letterCounter2 += 1
                    
            # Check if the length of category is sufficient (between 2 to 20 chars),
            # and that the category at least has 2 letters. If so, break out of loop.
            if len(category) >= 2 and len(category) <= 20 and letterCounter2 >= 2:
                break

            # Otherwise, print an error message.
            print("{}, enter a category with 2-20 characters and at least 2 letters.".format(makerName))

        # If the user is playing with partners, the player does not see the
        # puzzle and the screen is cleared (36 new lines) after the user presses
        # enter
        input("\nAnd now finally (please press enter)...")
        print("\n"*36)

    # Since the name of the player is asked whether the user enters 0 or another
    # number, the prompt to ask the player name is outside the if structure.
    # Makes the user aware that if no me is entered, their name will be "Guest"
    print("\nNOTE: your name will be 'Guest' if you don't enter a name.")

    # Asks the user their name and converts answer to capitalized if name is not
    # already capitalized.
    name = input("Enter name of player: ").title()

    # Checks to see if no name is entered
    # If so, set name to "Guest"
    if name == "":
        name = "Guest"

    # Make the user aware (in both cases, 0 or not) that they can only guess
    # incorrectly 6 times, and then, they lose. Player's name is formatted
    # into the statement.
    print("\n\nNOTE: {}, you lose if you make 6 incorrect guesses. Good luck {}!".format(name, name))

    # Call the PressEnter() function. Prompts the user to press enter to continue.
    # User name is formatted in the statement.
    PressEnter(name)
        
    # Start for loop which repeats for how long the puzzle is.
    for a in range(len(puzzle)):

        # Checks if there a letters (A-Z) in the puzzle. If so, the hidden
        # string is equal to itself plus an underscore and the numOfLetters
        # increments by 1.
        if puzzle[a] >= "A" and puzzle[a] <= "Z":
            hidden += "_"
            numOfLetters += 1

        # Otherwise, not a letter
        else:

            # Hidden is equal to itself plus whatever char there may be in puzzle
            hidden += puzzle[a]

    # start for loop to repeat for how long puzzle is
    for b in range(len(puzzle)):

        # print out one char of puzzle followed by a space. Used in print
        # statements with .format()
        spacedOut += puzzle[b] + " "

    # Start loop (actual game loop which is in action most of the time)        
    while True:

        # Call the FormatScreen() function which clears the screen and adds
        # underscores for formatting purposes
        FormatScreen()

        # Display hangman ASCII art
        # Since the hangman art and the value of wrong match perfectly, the
        # value of wrong is used to access the ASCII art array.
        print(hangman[wrong])

        # display all the letters the user guessed (right-justified)
        print("Letters guessed: ".rjust(80))
        print(guessedLetters.rjust(78))
        print()

        # Display all the incorrect letters the user guessed (right-justified)
        print("Incorrect letters: ".rjust(80))
        print(incorrectLetters.rjust(78))
        print()

        # Display all the letters that the player can still guess (right-justified) 
        print("Letters you can still guess: ".rjust(80))
        print(chooseLetter.rjust(79))
        print()

        # Displaying the amount of letters in the puzzle still to be guessed
        # by subtracting number of letters by the amount of letters that have
        # been revealed (right-justified)
        print("Num. of unrevealed letters in the puzzle: ".rjust(80))
        print("{:<77}{:2d}".format(" ", numOfLetters - hiddenLetters))
        print()

        # Display how many incorrect attempts are remaining (right-justified)
        print("Incorrect attempts remaining: ".rjust(80))

        # Use formatting to right justify
        print("{:<78}{:1d}".format(" ", wrong))
        print()
        print()

        # The following algorithm displays a blank phrase/ word (only underscore and/or
        # non-alpha are revealed) which is spaced out.
        # Start for loop which repeats for how long the hidden string is
        for j in range(len(hidden)):

            # Display that one char of hidden followed by a space
            print(hidden[j] + " ", end="")

        # Display what the category is.
        print("\nThe category is: {}".format(category))

        # start error trap for guess values (this loop is to check for already
        # guessed letters
        while True:

            # this loop is to check for length and values of guess
            while True:

                # Ask user for guess
                guess = input("\n{}, please enter your guess (enter 1 to guess entire puzzle): ".format(name)).upper()

                # Check if guess is between A-Z and length is 1, or guess is
                # equal to 1. If so, break out of loop.
                if guess >= "A" and guess <= "Z" and len(guess) == 1 or guess == "1":
                    break

                # Otherwise, print an error message
                print("Invalid guess! {}, Enter a guess between A - Z or enter 1 to solve.".format(name))

            # Check to see if guess is already in the guessedLetters string.
            # If so, display a message showing to change the guess to another letter
            if guessedLetters.find(guess) != -1:
                print("{}, you already guessed that letter. Guess another letter.".format(name))

            # Otherwise (guess not in guessedLetters string), break out of error trap loop    
            else:
                break

        # Check if guess is equal to 1
        if guess == "1":

            # If so, ask user to enter the entire solved puzzle (convert to uppercase)
            solvedPuzzle = input("Enter solved puzzle (including all the spaces and non-alpha characters if any):\n").upper()

            # Check to see if the user entered in the correct puzzle, if so,
            # clear and format the screen, and display a message which indicates
            # that the user has won. And break out of loop.
            if solvedPuzzle == puzzle:
                print("\n"*30)
                print("_"*80)
                print("")
                print("Congrats {}! You guessed it...\n".format(name))
                print(spacedOut)
                print("\n\nNumber of tries it took {} to win the game: {}".format(name, tries))
                print("YOU WON {}!".format(name))
                break

            # Otherwise, if guess is wrong, tell the user that, and tell user
            # what incorrect guess they are on.
            # Subtract one from the wrong variable
            else:
                print("Sorry {}, that is not the puzzle!".format(name))
                print("{}, that is your incorrect guess #{}.".format(name, 6-(wrong-1)))
                wrong -= 1

        # Otherwise (guess is a letter which is not already guessed before)
        else:

            # Add the guess to the guessedLetters string
            guessedLetters += guess

            # Start for loop which repeats for how long the chooseLetter string is.
            for i in range(len(chooseLetter)):

                # Check to see if that one char of chooseLetter if equal to guess
                if chooseLetter[i] == guess:

                    # If so, remove that letter by adding a space in its position
                    chooseLetter = chooseLetter[ :i] + " " + chooseLetter[i+1: ]

            # Start for loop which repeats for how long the puzzle is          
            for q in range(len(puzzle)):

                # Check if guess is equal to that one char of puzzle
                if guess == puzzle[q]:

                    # If it is, hidden will reveal that letter by adding that
                    # that specific guess and removing that underscore at that
                    # specific position.
                    hidden = hidden[ :q] + guess + hidden[q+1: ]

                    # Check if that one char of puzzle is not in the printed
                    # string. If not, display a message that the guess was
                    # found in the puzzle only ONCE.
                    # This stops the program from printing the success message
                    # the number of times there is that specific letter.
                    if printed.find(puzzle[q]) == -1:
                        print("Success! The letter \"{}\" is in the puzzle {}!".format(guess, name))

                    # Add guess to the printed string
                    printed += guess

                    # Add 1 to the hiddenLetters as a letter has been revealed
                    # in the hidden string
                    hiddenLetters += 1

            # Check if the guess is not in puzzle.
            if puzzle.find(guess) == -1:

                # If so, display a message indicating that.
                print("Sorry {}, the letter \"{}\" is not in the puzzle.".format(name, guess))
                # This print statement tells the user what incorrect guess they
                # are on. A special formula is developed to display that using
                # the value of the "wrong" variable
                print("{}, that is your incorrect guess #{}.".format(name, 6-(wrong-1)))

                # Add this incorrect guess to the incorrectLetters string
                incorrectLetters += guess

                # Subtract 1 from wrong
                wrong = wrong - 1

        # Calls the PressEnter() function prompts the user to press enter
        # to continue
        PressEnter(name)

        # Check if wrong is equal to 0
        if wrong == 0:

            # Call the FormatScreen() function which clears the screen and adds
            # underscores for formatting purposes
            FormatScreen()

            # display the hangman ASCII art
            print(hangman[wrong])

            # Following print statements display a losing message and the puzzle
            print("Sorry {}, you lose!".format(name))
            print("Sorry! You have been hanged!")
            print("{}, you reached the maximun of 6 incorrect guesses.".format(name))
            print("The puzzle was...\n\n{}".format(spacedOut))
            print("\n\nThanks for playing {}!".format(name))

            # break out of loop
            break

        # Check if hiddenLetters are equal to numOfLetters (winner)
        elif hiddenLetters == numOfLetters:
            
            # Call the FormatScreen() function which clears the screen and adds
            # underscores for formatting purposes
            FormatScreen()

            # Following print statements display a winning message and the puzzle
            print("")
            print(spacedOut)
            print("\n\nCONGRATS {}!!!\nYOU WON!".format(name))
            print("\n\nNumber of tries it took {} to win the game: {}".format(name, tries))
            print("\nThanks for playing {}!".format(name))

            # break out of loop
            break

        # Otherwise, not winner or loser
        else:

            # Increment tries by 1
            tries += 1

            # Add underscores to divide screen in sections for formatting purposes
            print("_"*80)

            # and the game loops

    # Start error trap for y or n values
    while True:

        # Ask user if they want to try again. Convert to all lowercase
        tryAgain = input("\n{}, want to play again (y or n)? ".format(name)).lower()

        # Check if user enters y, n, yes, or no. If so, break out of error trap loop.
        if tryAgain == "y" or tryAgain == "n" or tryAgain == "yes" or tryAgain == "no":
            break

        # Otherwise, display an error message
        print("{}, please enter y or n.".format(name))

    # Check if user entered n or no. If so, display ending remarks and break
    # out of program
    if tryAgain == "n" or tryAgain == "no":
        print("\n{}, thanks for playing, hope you had fun! See you later {}!!!".format(name, name))
        break

    # If user enters in y or yes, display a thanking message for playing again.
    print("Thanks for playing again {}! Enjoy!!!".format(name))

    # Calls the PressEnter function which prompts the user to press enter to continue
    PressEnter(name)

    # Clears the screen by adding new lines
    print("\n"*30)
